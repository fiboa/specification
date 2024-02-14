const path = require('path');
const fs = require('fs/promises');
const Ajv = require('ajv/dist/2020');
const addFormats = require('ajv-formats');
const axios = require('axios');
const YAML = require('yaml');
const yargs = require('yargs/yargs');
const { hideBin } = require('yargs/helpers');
const createSchema = require('./create_schema.js');

const ALLOWED_EXTENSIONS = ['.json', '.geojson', '.parquet', '.geoparquet'];

// Check if something is an object
function isObject(obj) {
	return (typeof obj === 'object' && obj === Object(obj) && !Array.isArray(obj));
}

function isHttp(uri) {
  return uri.startsWith("http://") || uri.startsWith("https://");
}

// Get config from CLI
function getConfig() {
	const config = yargs(hideBin(process.argv))
  .parserConfiguration({
    'camel-case-expansion': false,
    'boolean-negation': false,
    'strip-aliased': true
  })
  .option('verbose', {
    alias: 'v',
    type: 'boolean',
    default: false,
    description: 'Run with verbose logging.'
  })
  .option('collection', {
    alias: 'c',
    type: 'string',
    default: null,
    description: 'Points to the STAC collection that defines the fiboa version and extensions.'
  })
  .version()
  .parse()
  
  delete config.$0;

  return config;
}

// Read files from CLI
// Expands folders to files
async function getFiles(files) {
  const allFiles = [];
  // Check for folders and expand the contents to a list of files
  for(const file of files) {
    if (isHttp(file)) {
      allFiles.push(file);
      continue;
    }
    const stat = await fs.lstat(file);
    if (stat.isDirectory()) {
      const folderFiles = await fs.readdir(file);
      for (const folderFile of folderFiles) {
        // get extension
        const ext = path.extname(folderFile);
        if (ALLOWED_EXTENSIONS.includes(ext)) {
          allFiles.push(path.join(file, folderFile));
        }
      }
    }
    else {
      allFiles.push(file);
    }
  }
	return allFiles;
}

// Create ajv instance for validation
function createAjv(config) {
  // Create ajv instance for JSON Schema draft 2020-12 (used by fiboa)
	const instance = new Ajv({
		allErrors: config.verbose,
		logger: config.verbose ? console : false,
		loadSchema: loadFile
	});

  // Add support for draft-07 (used by GeoJSON)
  const draft7MetaSchema = require("ajv/dist/refs/json-schema-draft-07.json")
  instance.addMetaSchema(draft7MetaSchema);

  // Add additional formats
	addFormats(instance);

	return instance;
}

// Load schemas and data from filesystem or URL
async function loadFile(uri) {
  let parser;
  if (uri.endsWith(".yml") || uri.endsWith(".yaml")) {
    parser = YAML.parse;
  }
  else if (uri.endsWith(".json") || uri.endsWith(".geojson")) {
    parser = JSON.parse;
  }
  else {
    // Pass through
    parser = data => data;
  }
	if (isHttp(uri)) {
		let response = await axios.get(uri);
    if (response.data === 'string') {
      return parser(response.data);
    }
    else {
		  return response.data;
    }
	}
	else {
		return parser(await fs.readFile(uri, "utf8"));
	}
}

async function validate() {
	console.log(`fiboa GeoJSON Validator`);
	console.log();

  // Get config from CLI
  const config = getConfig();

  // Create ajv instance for validation
  const ajv = createAjv(config);

  // Expand folders to files
  const files = await getFiles(config._);
	if (files.length === 0) {
		throw new Error('No files found.');
	}

  // Load collection
  let collection = null;
  let version = require('../../package.json').version;
  let versionInfo = `unknown (assuming ${version})`;
  const extensions = {};
  let extensionInfo = "unknown";
  const extErrors = [];
  if (config.collection) {
    collection = await loadFile(config.collection);
    if (Array.isArray(collection.fiboa_extensions)) {
      for (const ext of collection.fiboa_extensions) {
        try {
          const extSchema = await loadFile(ext);
          const jsonSchema = createSchema(extSchema);
          extensions[ext] = await ajv.compileAsync(jsonSchema);
        } catch (error) {
          extensions[ext] = null;
          extErrors.push(`Failed to load extension ${ext}: ${error}`);
        }
      }
      extensionInfo = collection.fiboa_extensions.join(", ") || "none";
    }
    if (typeof collection.fiboa_version === 'string') {
      version = collection.fiboa_version;
      versionInfo = collection.fiboa_version;
    }
  }
  console.log("fiboa version: " + versionInfo);
  console.log("fiboa extensions: " + extensionInfo);
  if (extErrors.length > 0) {
    extErrors.forEach(error => console.log(error));
  }
  console.log();

  // Compile schema for validation
  const schema = await loadFile('core/schema/schema.yml');
  const jsonSchema = createSchema(schema);
  const ajvValidate = await ajv.compileAsync(jsonSchema);

  const markInvalid = (label, error, ext = null) => {
    if (ext) {
      console.log(`${label}: Extension ${ext} INVALID`);
    }
    else {
      console.log(`${label}: INVALID`);
    }
    console.log(error);
  };

  // Validate
  let count = 0;
  let validCount = 0;
  for(let file of files) {
    let data;
    try {
      data = await loadFile(file);
    } catch (error) {
      markInvalid(file, error);
      continue;
    }

    if (!isObject(data)) {
      markInvalid(file, 'Must be a JSON object');
      continue;
    }

    let features;
    if (data.type === "Feature") {
      features = [data];
    }
    else if (data.type === "FeatureCollection") {
      features = data.features;
    }
    else if (data.type === "Collection") {
      if (path.normalize(config.collection) !== path.normalize(file)) {
        console.log(`${file}: SKIPPED (is likely a STAC Collection)`);
      }
      continue;
    }
    else {
      markInvalid(file, 'Must be a GeoJSON Feature or FeatureCollection');
      continue;
    }

    if (features.length === 0) {
      markInvalid(file, 'Must contain at least one Feature');
      continue;
    }
    
    for(const index in features) {
      count++;
      const feature = features[index];
      const valid = ajvValidate(feature);

      let label = file;
      if (features.length > 1) {
        if (typeof feature.id === 'string') {
          label += ` (id: ${feature.id})`;
        }
        else {
          label += ` (index: ${index})`;
        }
      }
      if (!valid) {
        markInvalid(label, ajvValidate.errors);
      }
      else {
        for(const ext in extensions) {
          if (extensions[ext]) {
            const validExt = extensions[ext](feature);
            if (!validExt) {
              markInvalid(label, extensions[ext].errors, ext);
              valid = false;
            }
          }
          else {
            console.log(`${label}: Extension ${ext} SKIPPED`);
          }
        }
        if (valid) {
          console.log(`${label}: VALID`);
          validCount++;
        }
      }
      console.log();
    }
  }

  const invalid = count - validCount;
  if (invalid === 0) {
    console.log('=== All features are VALID ===');
  }
  else if (invalid === 1) {
    console.log(`=== 1 feature is INVALID ===`);
  }
  else {
    console.log(`=== ${invalid} features are INVALID ===`);
  }
}

validate()
  .then(() => process.exit(0))
  .catch(error => {
    console.error(error);
    process.exit(1);
  });