import json
import os
import pyarrow as pa
import pyarrow.types as pat

from .const import PA_TYPE_MAP, GP_TYPE_MAP
from .util import log, load_fiboa_schema
from geopandas import GeoDataFrame
from shapely.geometry import shape

def create(output_file):
  examples = [
    "geojson/examples/example.json"
  ]

  # Load all features from the GeoJSON files
  features = []
  for example in examples:
    with open(example, 'r') as f:
      geojson = json.loads(f.read())
      if geojson["type"] == "Feature":
        features.append(geojson)
      elif geojson["type"] == "FeatureCollection":
        features += geojson.features
      else:
        log(f"Unsupported GeoJSON type, must be Feature or FeatureCollection", "error")
        exit(1)

  # Load the data schema
  fiboa_schema = load_fiboa_schema()

  # Get a list of the properties/columns (without duplicates)
  columns = set(fiboa_schema["required"])
  for feature in features:
    keys = feature["properties"].keys()
    columns.update(keys)

  columns = list(columns)
  columns.sort()

  # Define the fields for the schema
  pq_fields = []
  for name in columns:
    try:
      pa_type = create_type(fiboa_schema["properties"][name])
      pq_fields.append(pa.field(name, pa_type))
    except Exception as e:
      log(f"{name}: {e}", "error")
      exit(1)

  # Define the schema for the Parquet file
  pq_schema = pa.schema(pq_fields)

  # Add a STAC collection to the fiboa property to the Parquet metadata
  with open(example, 'r') as f:
    collection = json.loads(f.read())
    collection["id"] = os.path.basename(output_file)
    # todo: fill with more/better metadata
  
  pq_schema = pq_schema.with_metadata({"fiboa": json.dumps(collection).encode("utf-8")})

  # Create GeoDataFrame from the features
  data = create_dataframe(features, columns, fiboa_schema)

  # Write the data to the Parquet file
  data.to_parquet(
    output_file,
    # todo: doesn't work: https://github.com/geopandas/geopandas/issues/3182
    # schema = pq_schema,
    index = False,
    coerce_timestamps = "ms"
  )

  log(f"Wrote to {output_file}", "success")

def create_dataframe(features, columns, schema):
  # Create a list of shapes
  rows = []
  for feature in features:
    id = feature["id"] if "id" in feature else None
    geometry = shape(feature["geometry"]) if "geometry" in feature else None
    row = {
      "id": id,
      "geometry": geometry,
    }
    properties = feature["properties"] if "properties" in feature else {}
    row.update(properties)
    rows.append(row)
  
  # Create the GeoDataFrame
  data = GeoDataFrame(rows, columns=columns)

  # Convert the data to the correct types
  for column in columns:
    dtype = schema["properties"][column].get("type", None)
    if dtype == "geometry":
      continue
    
    gp_type = GP_TYPE_MAP.get(dtype, None)
    if gp_type is None:
      log(f"{column}: No type conversion available for {dtype}")
    elif callable(gp_type):
      data[column] = gp_type(data[column])
    else:
      data[column] = data[column].astype(gp_type)

  return data

def create_type(schema):
  dtype = schema.get("type", None)
  if (dtype is None):
    raise Exception("No type specified")
  
  pa_type = PA_TYPE_MAP.get(dtype, None)
  if pa_type is None:
    raise Exception(f"{dtype} is not supported yet")
  elif callable(pa_type):
    if dtype == "array":
      pa_subtype = create_type(schema["items"])
      pa_type = pa_type(pa_subtype)
      pa_type.nullable = schema.get("optional", False)
    elif dtype == "object":
      pass # todo

  return pa_type
    