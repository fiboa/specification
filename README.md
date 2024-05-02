# Field Boundaries for Agriculture (fiboa) Specification

The Field Boundaries for Agriculture (fiboa) project is focused on making field boundary data openly available in a unified format on a global scale.
We believe that the fiboa specification is a foundational aspect of agricultural field boundary data interoperability
which enables and accelerates additional layers of collaboration and detail via custom extensions.
This repository contains the core specification for fiboa, including the data schema.
For more context, information on the ecosystem, and points of contact see the
[fiboa github organization](https://github.com/fiboa/).

- Version: **0.2.0**

> [!IMPORTANT]  
> The fiboa specification is a work in progress.
> Feedback is welcome and encouraged.
> You can follow our [CHANGELOG](https://github.com/fiboa/specification/blob/main/CHANGELOG.md) to track our progress.

## Key Features

The center of fiboa is the specification for representing field boundary data in GeoJSON & GeoParquet in a standard way,
with several optional extensions that specify additional attributes.
The core data schema of fiboa is quite simple: it’s a set of definitions for attribute names and values.
The number of attributes in the core is quite small by design.
The idea is that most of the ‘interesting’ data about the field will be located in extensions.

The specification in this repository consists of three parts:

- [Core Specification](core/README.md)
  (file format agnostic definition for data and metadata)
- [GeoJSON Encoding](geojson/README.md)
- [GeoParquet Encoding](geoparquet/README.md)

To completent the specification, there are also best practices and extensions available:

- [Best Practices](best-practices/README.md)
- [Extensions](https://github.com/fiboa/extensions/)

The repository also contains additional information about the project:

- [Changelog](CHANGELOG.md)
- [Citation Details (as CFF file)](CITATION.cff)

The fiboa community strives to provide a welcoming and transparent environment for all of the project’s participants.
You can find additional information about our community best practices and collaborative development processes below:
  
- [Code of Conduct](CODE_OF_CONDUCT.md)
- [Contribution Guideline](CONTRIBUTING.md)
- [Development and Release Process](process.md)
