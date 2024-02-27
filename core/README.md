# Core Specification

- **Schema:** <https://fiboa.github.io/specification/v0.0.2/schema.yaml>

**NOTE: The Core Specification is still work in progress.**

This specification describes the core data and metadata properties for both at the
Collection and Feature level.

- A Collection refers to a group of one or more features.
- A Feature is a single field geometry with additional properties.

A limited set of [data types](datatypes.md) have been defined so that a clear migration path
between encodings can be provided.

## Collections

Collection-level metadata must be provided in a STAC Collection that contains an
asset that points to fiboa-compliant Features.

The invidiual encodings may decide to embed the STAC Collection or make it available separately.

### Properties

| Property Name    | Data Type      | Description |
| ---------------- | -------------- | ----------- |
| fiboa_version    | string         | **REQUIRED.** Version number of the fiboa specification this entity implements. |
| fiboa_extensions | array\<string> | A list of URIs to extensions this entity implements. |

Generally, the version and the extensions must be uniform per Collection. 

## Features

### General Properties

| Property Name | Data Type | Description |
| ------------- | --------- | ----------- |
| id            | string    | **REQUIRED.** A unique identifier for the field. It must be unique within the Collection (see above). |
| collection    | string    | The identifier of the parent collection. |

The collection identifier is usually only needed for merged datasets.

### Spatial Properties

| Property Name | Data Type    | Description |
| ------------- | ------------ | ----------- |
| geometry      | geometry     | **REQUIRED.** A geometry that reflects the footprint of the field, usually a Polygon. Default CRS is WGS84. |
| bbox          | bounding-box | The bounding box of the field. |
| area          | uint32       | Area of the field, in ha. Must be > 0 and <= 1.000.000.000. This is simply a derived attribute from the geometry itself, and should match the geometry's area. If they do not match then the geometry should be considered canonical (and validators should flag when they don't match). |

### Temporal Properties

| Property Name        | Data Type | Description |
| -------------------- | --------- | ----------- |
| observation_datetime | datetime  | The last timestamp at which field did exist and was observed, in UTC and formatted according to RFC 3339, section 5.6. |

More temporal properties will be defined in a [timestamps extension](https://github.com/fiboa/extensions/issues/1).
