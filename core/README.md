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
| area          | float        | Area of the field, in hectares. Must be > 0 and <= 100,000. |
| perimeter     | float        | Perimeter of the field, in meters. Must be > 0 and <= 125,000. |

**area:** This is simply a derived attribute from the geometry itself,
and must match the geometry's area. If they do not match then the
geometry should be considered canonical.
Validators may flag the value as invalid if it exceeds a certain threshold.

### Determination Properties

| Property Name          | Data Type | Description |
| ---------------------- | --------- | ----------- |
| determination_method   | enum      | The boundary creation method, one of the values below. |
| determination_datetime | datetime  | The last timestamp at which the field did exist and was observed, in UTC. |

**determination_datetime**: In case the source of the information is an
interval or a set of timestamps, use the end.
For example, for ML you'd use the timestamp of the last image and not the
timestamp of the actual execution.

More temporal properties will be defined in a [timestamps extension](https://github.com/fiboa/extensions/issues/1).

**determination_method**: Allowed values:
- `manual` (hand drawn from imagery)
- `driven`
- `surveyed`
- `administrative`
- `auto-operation` (auto-created from operation)
- `auto-imagery` (auto-created from imagery)
- `unknown`
