# GeoParquet Encoding Specification

The Geoparquet encoding defines how field boundaries compliant to fiboa must be published.
The generic GeoParquet format is defined in the
[OGC GeoParquet specification v1.0.0](https://geoparquet.org/releases/v1.0.0/).
We aim to support any future version of GeoParquet, too.

> [!NOTE]
> The GeoParquet encoding is still work in progress. Feedback is welcome!

- **[Examples](examples/)**
- **[Data type mapping](datatypes.md)**

## Collection

The GeoParquet file must embed the [fiboa Collection](../core/README.md#collection)
in the Parquet metadata in a property named `fiboa`.

It is recommended to additionally provide the fiboa Collection as a separate JSON file, too.

## Features

Each [fiboa Feature](../core/README.md#features) corresponds to a row in a GeoParquet file.

The properties defined for fiboa Features are made available as individual columns in the GeoParquet file.

Properties that are optional can be omitted if all values are
[null values](https://parquet.apache.org/docs/file-format/nulls/),
i.e. the column can be missing from the GeoParquet file.

The mapping between the Parquet data types and the fiboa data types, can be found in the
[data type mapping](datatypes.md).

