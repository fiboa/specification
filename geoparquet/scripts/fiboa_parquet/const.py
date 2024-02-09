import pyarrow as pa
import pyarrow.types as pat
import pandas as pd

GP_TYPE_MAP = {
  "boolean": "bool",
  "int8": "int8",
  "uint8": "uint8",
  "int16": "int16",
  "uint16": "uint16",
  "int32": "int32",
  "uint32": "uint32",
  "int64": "int64",
  "uint64": "uint64",
  "float": "float32",
  "double": "float64",
  "binary": "bytearray", # todo: check
  "string": "str",
  "array": None, # todo: object?
  "object": "object",
  "enum": "category", # todo: check
  "date": "datetime64[D]",
  "date-time": lambda x: pd.to_datetime(x),
  "geometry": None, # not a column, don't convert geometry
  "bounding-box": None # todo
}

PA_TYPE_MAP = {
  "boolean": pa.bool_(),
  "int8": pa.int8(),
  "uint8": pa.uint8(),
  "int16": pa.int16(),
  "uint16": pa.uint16(),
  "int32": pa.int32(),
  "uint32": pa.uint32(),
  "int64": pa.int64(),
  "uint64": pa.uint64(),
  "float": pa.float32(),
  "double": pa.float64(),
  "binary": pa.binary(),
  "string": pa.string(),
  "array": lambda type: pa.list_(type),
  "object": None, # todo: lambda type: pa.map_(pa.string(), type)
  "enum": None, # todo: ENUM (BYTE_ARRAY)
  "date": pa.date32(),
  "date-time": pa.timestamp("ms", tz="UTC"),
  "geometry": pa.binary(),
  "bounding-box": None # todo
}

PA_TYPE_CHECK = {
  "boolean": pat.is_boolean,
  "int8": pat.is_int8,
  "uint8": pat.is_uint8,
  "int16": pat.is_int16,
  "uint16": pat.is_uint16,
  "int32": pat.is_int32,
  "uint32": pat.is_uint32,
  "int64": pat.is_int64,
  "uint64": pat.is_uint64,
  "float": pat.is_float32,
  "double": pat.is_float64,
  "binary": pat.is_binary,
  "string": pat.is_string,
  "array": pat.is_list,
  "object": pat.is_map,
  "enum": None, # ENUM (BYTE_ARRAY)
  "date": pat.is_date32,
  "date-time": pat.is_timestamp,
  "geometry": pat.is_binary, # todo: check more?
  "bounding-box": None # todo
}

LOG_STATUS_COLOR = {
  "info": "white",
  "warning": "yellow",
  "error": "red",
  "success": "green"
}
