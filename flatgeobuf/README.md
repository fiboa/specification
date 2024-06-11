# FlatGeobuf Encoding Specification

The FlatGeobuf encoding defines how field boundaries compliant to fiboa must be published.
The generic FlatGeobuf format is defined on the [FlatGeobuf website](https://flatgeobuf.org/).

> [!NOTE]
> The FlatGeobuf encoding is still work in progress. Feedback is welcome!

- **[Examples](examples/)**
- **[Data type mapping](datatypes.md)**

## Collection

The FlatGeobuf file must embed the [fiboa Collection](../core/README.md#collection) into the `Header` table's 
[`metadata`](https://github.com/flatgeobuf/flatgeobuf/blob/ee7c8f5f45c67dd4a84a51fef518dfebc3e19d0a/src/fbs/header.fbs#L81) 
field in a property named `fiboa` within a JSON-structured object.
It is recommended to also provide the fiboa Collection as a separate JSON file.

> [!NOTE]
> Starting in GDAL/OGR 3.9.0 the [FlatGeobuf driver](https://gdal.org/drivers/vector/flatgeobuf.html)
supports writing to the Header's `metadata` field with the `-mo` option, i.e. `-mo "fiboa_version=0.2.0"`.

## Features

Each [fiboa Feature](../core/README.md#features) corresponds to a Flatbuffer record in the 
[`Feature`](https://github.com/flatgeobuf/flatgeobuf/blob/ee7c8f5f45c67dd4a84a51fef518dfebc3e19d0a/src/fbs/feature.fbs#L16-L20)
table of a FlatGeobuf file.

All properties defined for fiboa Features, except the Geometry, are made available as the 
[`properties`](https://github.com/flatgeobuf/flatgeobuf/blob/ee7c8f5f45c67dd4a84a51fef518dfebc3e19d0a/src/fbs/feature.fbs#L18) 
vector of a FlatGeobuf Feature. Key names and data types are encoded into the 
[Header's `columns`](https://github.com/flatgeobuf/flatgeobuf/blob/ee7c8f5f45c67dd4a84a51fef518dfebc3e19d0a/src/fbs/header.fbs#L75) schema.

Properties that are optional can be omitted if all values are
[null values](https://github.com/flatgeobuf/flatgeobuf/blob/ee7c8f5f45c67dd4a84a51fef518dfebc3e19d0a/src/fbs/header.fbs#L52)
i.e. the column can be missing from the FlatGeobuf file.

The mapping between the 
[FlatGeobuf data types](https://github.com/flatgeobuf/flatgeobuf/blob/ee7c8f5f45c67dd4a84a51fef518dfebc3e19d0a/src/fbs/header.fbs#L26-L42)
and the fiboa data types, can be found in the [data type mapping](datatypes.md).

