import json
import pyarrow.parquet as pq
import pyarrow.types as pat

from yaml import safe_load as yaml_load
from jsonschema.validators import Draft7Validator
from pyarrow.fs import FSSpecHandler, PyFileSystem
from fsspec.implementations.local import LocalFileSystem
from .const import PA_TYPE_CHECK
from .util import log, load_fiboa_schema

def load_parquet_schema(url_or_path: str) -> pq.ParquetSchema:
  """Load schema from local Parquet file"""
  pyarrow_fs = PyFileSystem(FSSpecHandler(LocalFileSystem()))
  return pq.read_schema(pyarrow_fs.open_input_file(url_or_path))


def validate_schema(obj, schema, name):
  if isinstance(obj, str) or isinstance(obj, bytes) or isinstance(obj, bytearray):
    obj = json.loads(obj)

  errors = Draft7Validator(schema).iter_errors(obj)

  for error in errors:
    log(f"{name}: {error.json_path}: {error.message}", "warning")
    if "description" in error.schema:
      log(f"    \"{error.schema['description']}\"", "warning")

  return len(errors) > 0


def validate(input_file):
  valid = True
  parquet_schema = load_parquet_schema(input_file)

  if b"geo" not in parquet_schema.metadata:
    log("Parquet file schema does not have 'geo' key", "error")
    exit(1)
  else:
    # ToDo: We are not checking whether this is a valid GeoParquet file
    # We just check whether a geo key is present at all.
    # use gpq validate geoparquet metadata for now
    log(f"This validator doesn't check whether this file contains valid GeoParquet metadata, use gpq in addition.", "warning")
  
  if b"fiboa" not in parquet_schema.metadata:
    log("Parquet file schema does not have 'fiboa' key", "error")
    # don't exit until https://github.com/geopandas/geopandas/issues/3182 is solved
    # exit(1)
  else:
    # ToDo: We are not checking whether this is a valid STAC Collection file
    # We just check whether a fiboa key is present at all.
    log(f"This validator doesn't check whether this file contains a valid STAC Collection.", "warning")

  # load the actual fiboa schema
  fiboa_schema = load_fiboa_schema()
  properties = fiboa_schema["properties"]

  # Validate whether the Parquet schema complies with the property schemas
  for key in parquet_schema.names:
    # Ignore fields without a schema
    if key not in properties:
      log(f"{key}: No schema defined")
      continue

    prop_schema = properties[key]
    # Make sure the schema has a data type assigned
    dtype = prop_schema.get("type", None)
    if (dtype is None):
      log(f"{key}: No type specified", "warning")
      continue

    pq_field = parquet_schema.field(key)
    pq_type = pq_field.type
    
    # Does the field (dis)allow null?
    optional = prop_schema.get("optional", False)
    if optional != pq_field.nullable:
      log(f"{key}: Nullability differs, is {pq_field.nullable} but must be {optional}", "error")
      valid = False
    
    # Is the data type of the field correct?
    pa_check = PA_TYPE_CHECK.get(dtype, None)
    if pa_check is None:
      log(f"{key}: Validating {dtype} is not supported yet", "warning")
      continue
    elif not pa_check(pq_type):
      log(f"{key}: Data type invalid, is {pq_type} but must be {dtype}", "error")
      valid = False
      continue

    # Check specifics of some types
    if dtype == "date-time":
      if pq_type.unit != "ms":
        log(f"{key}: Timestamp unit differs, should be ms", "warning")
      if pq_type.tz != "UTC":
        log(f"{key}: Timestamp timezone invalid, must be UTC", "error")
        valid = False
    elif dtype == "object":
      if not pat.is_string(pq_field.key_type):
        log(f"{key}: Map key datatype is not string", "error")
        valid = False

  # validate_schema(parquet_schema.metadata[b"fiboa"], fiboa_schema, "fiboa")

  if valid:
    log("This is a valid fiboa file.\n", "success")
  else:
    log("This is an invalid fiboa file.\n", "error")
    exit(1)
