const YAML = require('yaml');
const fs = require('fs');

const propertiesYaml = fs.readFileSync('core/schema/schema.yml', 'utf8');
const properties = YAML.parse(propertiesYaml).properties;
const datatypesJson = fs.readFileSync('geojson/schema/datatypes.json', 'utf8');
const datatypes = JSON.parse(datatypesJson).$defs;

const geojsonCore = ['id', 'geometry', 'bbox', 'properties'];
const geojsonRootRequired = geojsonCore;

let geojsonRoot = {};
let geojsonProperties = {};
for (const key in properties) {
  const propSchema = properties[key];
  const combinedSchema = convertSchema(propSchema);

  // Assign it to the root or properties object
  if (geojsonCore.includes(key)) {
    geojsonRoot[key] = combinedSchema;
  } else {
    geojsonProperties[key] = combinedSchema;
  }
}

const schemaJson = fs.readFileSync('geojson/scripts/template.json', 'utf8');
const schema = JSON.parse(schemaJson);
schema.required = geojsonRootRequired;
schema.properties.id = geojsonRoot.id;
schema.properties.geometry = geojsonRoot.geometry;
schema.properties.bbox = geojsonRoot.bbox;
schema.properties.properties.properties = geojsonProperties;

fs.writeFileSync('geojson/schema/schema.json', JSON.stringify(schema, null, 2));

function isObject(item) {
  return (item && typeof item === 'object' && !Array.isArray(item));
}

// merge the schema of the property into the schema for the data type if refers to
function convertSchema(propSchema) {
  if (!isObject(propSchema) || typeof propSchema.type === 'undefined') {
    return propSchema;
  }
  else if (typeof datatypes[propSchema.type] === 'undefined') {
    throw new Error(`Unknown datatype ${propSchema.type}`);
  }

  const datatypeSchema = Object.assign({}, datatypes[propSchema.type]);

  // Allow null if the property is optional
  if (propSchema.optional === true) {
    if (typeof datatypeSchema.type === "string") {
      datatypeSchema.type = [datatypeSchema.type, "null"];
    } else if (Array.isArray(datatypeSchema.type)) {
      datatypeSchema.type.push("null");
    } else if (Array.isArray(datatypeSchema.oneOf)) {
      datatypeSchema.oneOf.push({type: "null"});
    } else if (Array.isArray(datatypeSchema.anyOf)) {
      datatypeSchema.anyOf.push({type: "null"});
    } else {
      throw new Error(`Making schema ${JSON.stringify(datatypeSchema)} optional is not supported by this generator`);
    }
  }

  // Avoid conflicting statements
  if (typeof propSchema.exclusiveMaximum !== 'undefined') {
    delete datatypeSchema.maximum;
  }
  if (typeof propSchema.exclusiveMinimum !== 'undefined') {
    delete datatypeSchema.minimum;
  }
  if (typeof propSchema.maximum !== 'undefined') {
    delete datatypeSchema.exclusiveMaximum;
  }
  if (typeof propSchema.minimum !== 'undefined') {
    delete datatypeSchema.exclusiveMinimum;
  }

  // deep merge schemas
  for (const key in propSchema) {
    const value = propSchema[key];
    if (key === 'items' && isObject(value)) {
      // Merge item schemas
      datatypeSchema.items = Object.assign(
        {},
        datatypeSchema.items,
        convertSchema(value)
      );
    }
    else if (key === 'properties' && isObject(value.properties)) {
      // Merge schemas for all properties
      if (!isObject(datatypeSchema.properties)) {
        datatypeSchema.properties = {};
      }
      for(const propName in value) {
        datatypeSchema.properties[propName] = Object.assign(
          {},
          datatypeSchema.properties[propName],
          convertSchema(value[propName])
        );
      }
    }
    else if (!['type', 'optional'].includes(key)) {
      datatypeSchema[key] = value;
    }
    // else: ignore
  }

  return datatypeSchema;
}