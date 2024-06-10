# FlatGeobuf Encoding Specification

The FlatGeobuf encoding defines how field boundaries compliant to fiboa must be published.
The generic FlatGeobuf format is defined on the [FlatGeobuf website](https://flatgeobuf.org/).
We aim to support any future version of Flatgeobuf, too.

> [!NOTE]
> The FlatGeobuf encoding is still work in progress. Feedback is welcome!

- **[Examples](examples/)**
- **[Data type mapping](datatypes.md)**

## Collection

The FlatGeobuf file must embed the [fiboa Collection](../core/README.md#collection) 
in the `Header` table's [`metadata`](https://github.com/flatgeobuf/flatgeobuf/blob/ee7c8f5f45c67dd4a84a51fef518dfebc3e19d0a/src/fbs/header.fbs#L81) 
field in a property named `fiboa` within a JSON-structured object.

It is recommended to additionally provide the fiboa Collection as a separate JSON file, too.

## Features

Each [fiboa Feature](../core/README.md#features) corresponds to a Flatbuffer record in the 
[`Feature`](https://github.com/flatgeobuf/flatgeobuf/blob/ee7c8f5f45c67dd4a84a51fef518dfebc3e19d0a/src/fbs/feature.fbs#L16-L20)
table of a FlatGeobuf file.

The properties defined for fiboa Features are made available as the 
[`properties`](https://github.com/flatgeobuf/flatgeobuf/blob/ee7c8f5f45c67dd4a84a51fef518dfebc3e19d0a/src/fbs/feature.fbs#L18) 
vector of a FlatGeobuf Feature. Keys and data types are encoded into the 
[`columns`](https://github.com/flatgeobuf/flatgeobuf/blob/ee7c8f5f45c67dd4a84a51fef518dfebc3e19d0a/src/fbs/feature.fbs#L19)
schema.

Properties that are optional can be omitted if all values are
[null values](https://github.com/flatgeobuf/flatgeobuf/blob/ee7c8f5f45c67dd4a84a51fef518dfebc3e19d0a/src/fbs/header.fbs#L52)
i.e. the column can be missing from the FlatGeobuf file.

The mapping between the 
[FlatGeobuf data types](https://github.com/flatgeobuf/flatgeobuf/blob/ee7c8f5f45c67dd4a84a51fef518dfebc3e19d0a/src/fbs/header.fbs#L26-L42)
and the fiboa data types, can be found in the [data type mapping](datatypes.md).


