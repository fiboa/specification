# Core Specification

This specification describes the core data and metadata properties for both at the
Collection and Feature level.

- A Collection refers to a group of one or more features.
- A Feature is a single field geometry with additional properties.

> [!NOTE]
> The Core Specification is still work in progress. Feedback is welcome!

- **Schema:** <https://fiboa.github.io/specification/v0.2.0/schema.yaml>

## Schema

The data types in the following document are defined in
[fiboa Schema](https://github.com/fiboa/schema), v0.1.0.

fiboa Schema defines a (limited) set of data types and a vocabulary to express
additional constraints for these data types.
This allows to define a clear mapping between the core specification and its encodings.

- [Data types](https://github.com/fiboa/schema/blob/v0.1.0/datatypes.md)
- [Vocabulary](https://github.com/fiboa/schema/blob/v0.1.0/README.md#vocabulary)

## Collection

Collection-level metadata must be provided in an object that contains the properties below.
The invidiual encodings may decide to embed the collection or make it available separately.

### Properties

| Property Name    | Data Type      | Description |
| ---------------- | -------------- | ----------- |
| fiboa_version    | string         | **REQUIRED.** Version number of the fiboa specification this entity implements. |
| fiboa_extensions | array\<string> | A list of URIs to extensions this entity implements. |

Generally, the version and the extensions must be uniform per Collection.

Other properties are also allowed to be provided, but are not described by this specification.

## Features

### General Properties

| Property Name  | Data Type | Description |
| -------------- | --------- | ----------- |
| id             | string    | **REQUIRED.** A unique identifier for the field. It must be unique within the [Collection](#collection). |
| collection     | string    | The identifier of the parent collection. |
| administrative | boolean   | Determines whether the boundary is coming from an official (usually governmental) source. |

The collection identifier is usually only needed for merged datasets.

### Spatial Properties

| Property Name | Data Type    | Description |
| ------------- | ------------ | ----------- |
| geometry      | geometry     | **REQUIRED.** A geometry that reflects the footprint of the field, usually a Polygon. Default CRS is WGS84. |
| bbox          | bounding-box | The bounding box of the field. |
| area          | float        | Area of the field, in hectares. Must be > 0 and <= 100,000. |
| perimeter     | float        | Perimeter of the field, in meters. Must be > 0 and <= 125,000. |

**area/perimeter:** These are derived attributes from the geometry itself,
and must match the geometry's area/perimeter. If they do not match then the
geometry should be considered canonical.
Validators may flag the value as invalid if it exceeds a certain threshold.

### Determination Properties

| Property Name          | Data Type | Description                                                  |
| ---------------------- | --------- | ------------------------------------------------------------ |
| determination_method   | string    | The boundary creation method, one of the values below.       |
| determination_datetime | datetime  | The last timestamp at which the field did exist and was observed, in UTC. |
| determination_details  | string    | Further details about the determination, especially the methodology. |

**determination_datetime**: In case the source of the information is an
interval or a set of timestamps, use the end.
For example, for ML you'd use the timestamp of the last image and not the
timestamp of the actual execution.

> [!NOTE]  
> We define more temporal properties in the
> [timestamps extension](https://github.com/fiboa/timestamps).

**determination_method**: Allowed values:

- `manual`: Hand created from imagery, e.g. using a tool to point and click on a map.
- `surveyed`: Determined through a professional land survey measuring the actual distances and angles on the ground.
- `driven`: An operator physically drove (or walked) around the perimeter of the field with a geopositioning device (e.g. GPS) that records the path taken. The operator actively and explicitly selected in the terminal to create a boundary.
- `auto-operation`: Automatically created from operation. Similar to driven but it is an implicit result of normal agricultural operations, so this is usually using the coverage map to determine the boundary.
- `auto-imagery`: Automatically created from aerial or satellite imagery, e.g. using CV or ML techniques.
- `unknown`: The default value. This often means it is defined by some other authority (see `administrative`) and is likely one of the other methods but there's no knowledge of which exactly.
