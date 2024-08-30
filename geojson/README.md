# GeoJSON Encoding Specification

The GeoJSON encoding defines how field boundaries compliant to fiboa must be published.
The generic GeoJSON format is defined in
[IETF RFC 7946](https://datatracker.ietf.org/doc/html/rfc7946).

> [!NOTE]
> The GeoJSON encoding is still work in progress. Feedback is welcome!

- **[Examples](examples/):**
  1. [as a FeatureCollection](examples/featurecollection/features.json)
  2. [as individual Features with a dedicated Collection](examples/individual-features/)
- **[Datatype mapping](datatypes.md)**

## FeatureCollection

A FeatureCollection may have a top-level property named `fiboa`.
If present, it contains all properties that are common across the features.
In validation they must be copied to the `properties` in each Feature.
All features in a FeatureCollection must be fiboa-compliant.

## Feature

Each [fiboa Feature](../core/README.md#features) must be a valid
[GeoJSON Feature](https://datatracker.ietf.org/doc/html/rfc7946#section-3.2).

The following properties are defined for a GeoJSON Feature (at the top-level of the object):

| Property Name | Data Type           | Description                                                  |
| ------------- | ------------------- | ------------------------------------------------------------ |
| id            | string              | **REQUIRED.** See [id](../core/README.md#general-properties) in the core specification, must not be a `number` |
| type          | string              | **REQUIRED.** The GeoJSON type, must be: `Feature`          |
| geometry      | object              | **REQUIRED.** A [GeoJSON Geometry Object](https://datatracker.ietf.org/doc/html/rfc7946#section-3.1), must not be `null` |
| bbox          | array\<number>      | A [GeoJSON Bounding Box](https://datatracker.ietf.org/doc/html/rfc7946#section-5) |
| properties    | object              | An object with all additional properties (see [`properties`](#properties)) |
| links         | array\<Link Object> | A list of links (see [`links`](#links))                      |

> [!IMPORTANT]  
> RFC 7946 doesn't support a property named `crs`, which was only available in an earlier version of GeoJSON (2008).
> The CRS of the GeoJSON geometry and bbox must be WGS 84 / OGC CRS 84,
> see the [RFC 7946, chapter 4](https://datatracker.ietf.org/doc/html/rfc7946#section-4) for details. 

### `properties`

Must include any property that is required by the fiboa core specification (currently `fiboa_version`).
May include any additional property.
All properties defined by the core specification (except for `id`, `geometry` and `bbox`) or extensions should be provided here.

### `links`

An array of links where each link conforms to the
[Hyperlink Schema](http://schemas.opengis.net/ogcapi/common/part1/1.0/openapi/schemas/link.yaml)
defined in
[OGC API - Common - Part 1](https://docs.ogc.org/is/19-072/19-072.html#_11b9b4f7-42fc-413a-b63a-e7fb060b5e4b).

The following relation types are commonly used:

- `self`: Absolute link to the GeoJSON file itself.
