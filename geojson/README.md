# GeoJSON Encoding Specification

The GeoJSON encoding defines to encode field boundaries compliant to fiboa as
GeoJSON as defined in [IETF RFC7946](https://datatracker.ietf.org/doc/html/rfc7946).

A single fiboa Feature must be encoded as a GeoJSON [`Feature`](#feature).
Multiple fiboa Featurs should be provided as a GeoJSON [`FeatureCollection`](#featurecollection).
Other GeoJSON types are not allowed.

Related documents:

- [Examples](examples/)
- [Datatype mapping](datatypes.md)

## Feature

- Example: [individual features](examples/individual-features/)

Each [fiboa Feature](../core/README.md) must be a valid
[GeoJSON Feature](https://datatracker.ietf.org/doc/html/rfc7946#section-3.2).

The following properties are defined for a GeoJSON Feature (at the top-level of the object):

| Property Name | Data Type           | Description |
| ------------- | ------------------- | ----------- |
| id            | string              | **REQUIRED.** See [id](../core/README.md#id) in the core specification, must not be a `number` |
| type          | string              | **REQUIRED.** The GeoJSON type, must be: `Feature` |
| geometry      | object              | **REQUIRED.** A [GeoJSON Geometry Object](https://datatracker.ietf.org/doc/html/rfc7946#section-3.1), must not be `null` |
| bbox          | array\<number>      | A [GeoJSON Bounding Box](https://datatracker.ietf.org/doc/html/rfc7946#section-5) |
| properties    | object              | An object with all additional properties (see [`properties`](#properties)) |

The mapping between the Parquet data types and the fiboa data types, can be found in the
[data type mapping](datatypes.md).

> [!IMPORTANT]  
> RFC 7946 doesn't support a property named `crs`, which was only available in an earlier version of GeoJSON (2008).
> The CRS of the GeoJSON geometry and bbox must be WGS 84 / OGC CRS 84,
> see the [RFC 7946, chapter 4](https://datatracker.ietf.org/doc/html/rfc7946#section-4) for details.

[Collection-level](../core/README.md#collection) data is not supported.
All properties are provides in the JSON object with the key [`properties`](#properties).

### properties

Must include any property that is required by the fiboa core specification.
May include any additional property.
All properties defined by the core specification (except for `id`, `geometry` and `bbox`) or extensions should be provided here.

## FeatureCollection

- Example: [a feature collection](examples/featurecollection/features.json)

All features in a GeoJSON FeatureCollection must be fiboa-compliant.

Properties can also be stored at the [collection-level](../core/README.md#collection)
if all values for a specific property have the same value in all features.
This de-duplicates data for more efficient resource usage.
All properties are stored on the top-level of the FeatureCollection object as
[foreign members](https://datatracker.ietf.org/doc/html/rfc7946#section-6.1).
The individual features shall not contain any properties that are stored at the collection-level.
Validation must ensure that the collection-level properties are taken into account.

The following properties in Features can't be collection-level properties:

- `id`
- `geometry`
- `bbox`

Properties with the following names can#t be moved to the collection-level due to conflicts with the
FeatureCollection properties defined by GeoJSON:

- `features`
- `type`
