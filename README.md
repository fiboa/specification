# Field Boundaries for Agriculture (fiboa) Specification

The Field Boundaries for Agriculture (fiboa) project is focused on making field boundary data openly available in a unified format on a global scale.
We believe that the fiboa specification is a foundational aspect of agricultural field boundary data interoperability
which enables and accelerates additional layers of collaboration and detail via custom extensions.
This repository contains the core specification for fiboa, including the data schema.
For more context, information on the ecosystem, and points of contact see the
[fiboa github organization](https://github.com/fiboa/).

- Version: **0.3.0**

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

The specification in this repository consists of just one fudamental part:

- [Core Specification](core/README.md) - file format agnostic definition for data and metadata
- [Examples](examples/) - GeoJSON and GeoParquet examples

It can be enriched by extensions and there's a
[list of extensions](https://vecorel.org/extensions/).

> [!NOTE]  
> Internally, the fiboa specification is an extension to the Vecorel ecosystem and
> is fully compatible with it. In fact, Vecorel and fiboa share significant portions of
> the extensions and tooling.

## Relation to other standards and working groups

fiboa doesn't aim to reinvent the wheel.
Our aim is to align with existing efforts as much as possible.
Some parts of the specification are already based on the work of other initiatives,
e.g. the determination-related fields in the core specification.

Related standards and working groups are:

- [Vecorel](https://vecorel.org)
- [Adapt standard](https://adaptstandard.org), including their [WG17](https://github.com/ADAPT/Standard/issues/97)
- [Varda FieldID](https://www.varda.ag/global-field-id)
- [Deere Boundaries](https://developer.deere.com/dev-docs/boundaries)
- [AgGateway](https://aggateway.org/), including their
  [Locking in on Field Boundaries](https://aggateway.org/Portals/1010/WebSite/About%20Us/FIELD%20BOUNDARY%20FLYER%20122123.pdf?ver=2024-01-03-212959-590) initiative

If you think we are missing relevant work here, we'd love to hear from you.
Please get in touch by [opening an issue](https://github.com/fiboa/specification/issues/new)!

## Contributing

The fiboa community strives to provide a welcoming and transparent environment for all of the project’s participants.
You can find additional information about our community best practices and collaborative development processes below:
  
- [Code of Conduct](https://vecorel.org/code-of-conduct/)
- [Contribution Guideline](CONTRIBUTING.md)
- [Development and Release Process](https://github.com/vecorel/specification/blob/main/process.md)
