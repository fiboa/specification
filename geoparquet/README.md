# Geoparquet Encoding Specification

- **[Examples](examples/)**
- **[Data type mapping](datatypes.md)**

**NOTE: The GeoParquet encoding is still work in progress. Feedback is always welcome!**

## Collection

The GeoParquet file must embed the [fiboa Collection](../core/README.md#collection)
in the Parquet metadata in a property named `fiboa`.

It is recommended to additionally provide the fiboa Collection as a separate JSON file, too.

## Feature Properties

The properties defined for [fiboa Features](../core/README.md#features) are made available as
individual columns in the GeoParquet file.

The mapping between the Parquet data types and the fiboa data types, can be found in the
[data type mapping](datatypes.md).

Properties that are optional can be omitted if all values are
[null values](https://parquet.apache.org/docs/file-format/nulls/).
