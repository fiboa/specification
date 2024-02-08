# Geoparquet Encoding

- [Examples](examples/)

**NOTE: The GeoParquet encoding is still work in progress.**

## Specification

## Collection Properties

Collection-level metadata must be provided as a STAC Collection.

The GeoParquet file must embed the STAC Collection in the file-level Parquet metadata in a property
named `fiboa`.

It is recommended to provide the STAC Collection as a separate JSON file, too.
In this case the STAC Collection should contain an asset pointing to the GeoParquet file.

## Feature Properties

Feature-level data and metadata refers to individual columns in the Parquet file.
