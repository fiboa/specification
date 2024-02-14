# GeoJSON Encoding

- **[Examples](examples/)**
- **Schema:** <https://fiboa.github.io/specification/v0.0.1/geojson/schema.json>

**NOTE: The GeoJSON encoding is still work in progress.**

## Specification

## Collection Properties

Collection-level metadata must be provided as a STAC Collection.

The GeoJSON FeatureCollection must embed the STAC Collection in a top-level property named `fiboa`.

*NOTE: According to the GeoJSON specification this is called a "foreign member" and must be
provided at the top-level. It can't be provided in properties due to:
[RFC7946, sec. 7.1](https://datatracker.ietf.org/doc/html/rfc7946#section-7.1):*
> FeatureCollection \[...] objects \[...] MUST NOT contain a \[...] "properties" member.*

It is recommended to provide the STAC Collection as a separate JSON file, too.
In this case the STAC Collection should contain an asset pointing to the GeoJSON FeatureCollection.

All Features in the FeatureCollection must be fiboa-compliant.

Collection-level metadata should **not** be specified in a GeoJSON FeatureCollection
due to [RFC7946, sec. 7.1](https://datatracker.ietf.org/doc/html/rfc7946#section-7.1): 

## Feature Properties

Feature-level data and metadata refers to a single GeoJSON Feature.

The following properties are provided in the GeoJSON document at the top-level:
- id
- geometry
- bbox

All other properties reside in the GeoJSON `properties`.
