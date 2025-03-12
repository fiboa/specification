# GeoParquet Encoding Specification

The Geoparquet encoding defines how field boundaries compliant to fiboa must be published.
The generic GeoParquet format is defined in the OGC GeoParquet specification,
either version [v1.0.0](https://geoparquet.org/releases/v1.0.0/)
or [v1.1.0](https://geoparquet.org/releases/v1.1.0/).
We aim to support any future version of GeoParquet, too.

Each [fiboa Feature](../core/README.md) corresponds to a row in a GeoParquet file.

The properties defined for fiboa Features are made available as individual columns in the GeoParquet file.

Properties that are optional can be omitted if all values are
[null values](https://parquet.apache.org/docs/file-format/nulls/),
i.e. the column can be missing from the GeoParquet file.

Properties can also be stored at the [collection-level](../core/README.md#collection) if all values in a column have the same value.
This de-duplicates data for more efficient resource usage and simplifies the sturcture of the Parquet file.
The GeoParquet file must embed the properties in the Parquet metadata in a property named `collection`.
The metadata must be JSON-encoded.

The mapping between the Parquet data types and the fiboa data types, can be found in the
[data type mapping](datatypes.md).

Related documents:

- [Examples](examples/)
- [Data type mapping](datatypes.md)

## Best practices

For data with a lot of repetition, brotli compression is recommended.
This applies particularly for merged datasets that don't deduplicate properties to the collection-level.
