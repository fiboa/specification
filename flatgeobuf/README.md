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
in the header's `metadata` field in a property named `fiboa` within a JSON-structured object.

It is recommended to additionally provide the fiboa Collection as a separate JSON file, too.

## Features

[WIP]

