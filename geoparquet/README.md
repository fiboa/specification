# Geoparquet Encoding Specification

- **[Examples](examples/)**
- **[Datatype mapping](datatypes.md)**

**NOTE: The GeoParquet encoding is still work in progress. Feedback is always welcome!**

## Collection

The GeoParquet file must embed the [fiboa Collection](../core/README.md#collection)
in the Parquet metadata in a property named `fiboa`.

It is recommended to provide the fiboa Collection as a separate JSON file, too.

## Feature Properties

Feature-level data and metadata refers to individual columns in the Parquet file.
