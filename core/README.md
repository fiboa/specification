# Core Specification

**NOTE: The Core Specification is still work in progress.**

This specification describes the core data and metadata properties for both at the
Collection and Feature level.

- A Collection refers to a group of one or more features.
- A Feature is a single field geometry with additional properties.

## Collections


Collection-level metadata must be provided in a STAC Collection that contains an
asset that points to fiboa-compliant Features.

The invidiual encodings may decide to embed the STAC Collection or make it available separately.

### Properties

| Property Name    | Data Type | Description |
| ---------------- | --------- | ----------- |
| fiboa_version    | string    | **REQUIRED.** Version number of the fiboa specification this entity implements. |
| fiboa_extensions | \[string] | A list of URIs to extensions this entity implements. |

Generally, the version and the extensions must be uniform per Collection. 

## Features

### General Properties

| Property Name | Data Type | Description |
| ------------- | --------- | ----------- |
| id            | string    | **REQUIRED.** A unique identifier for the field. |

### Spatial Properties

| Property Name | Data Type | Description |
| ------------- | --------- | ----------- |
| geometry      | object    | **REQUIRED.** A geometry that reflects the footprint of the field, usually a Polygon. Default CRS is WGS84. |
| bbox          | \[number] | The bounding box of the field. |
| area          | number    | Area of the field, in ha and > 0. |

### Temporal Properties

| Property Name | Data Type | Description |
| ------------- | --------- | ----------- |
| datetime      | string    | The data is valid since the given date and time (inclusive), in UTC and formatted according to RFC 3339, section 5.6. |
| expires       | string    | The data is valid until the given date and time (exclusive), in UTC and formatted according to RFC 3339, section 5.6. |

