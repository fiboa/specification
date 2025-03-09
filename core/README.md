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
[fiboa Schema](https://github.com/fiboa/schema), v0.2.0.

fiboa Schema defines a (limited) set of data types and a vocabulary to express
additional constraints for these data types.
This allows to define a clear mapping between the core specification and its encodings.

- [Data types](https://github.com/fiboa/schema/blob/v0.2.0/datatypes.md)
- [Vocabulary](https://github.com/fiboa/schema/blob/v0.2.0/README.md#vocabulary)

## General Properties

| Property Name | Data Type      | Description |
| ------------- | -------------- | ----------- |
| schemas       | array\<string> | **REQUIRED.** A list of URLs to schemas the collection implements. |
| id            | string         | **REQUIRED.** A unique identifier for the field. It must be unique per collection, i.e. `collection` and `id` form a unique identifier. |
| collection    | string         | The identifier of the parent collection. |
| category      | array\<string> | A set of categories the field boundary belongs to. |

**schemas:** The schemas the collection implements. Must be URLs to the schema YAML files.

The schema for this specification (see above) is required to be provided.

**collection:** The collection identifier is usually only needed for merged datasets.

**category:** Choose any (unique) combination of the following values:

- `conceptual`: This boundary represents how the grower thinks of a field, and what they would share with service
  providers to allocate information at the highest level of the field concept within their operation.
- `operational`: This boundary represents a management area used for a specific set of field operations as
  defined by or for the grower and is shared with service providers for field operation execution, analysis, or recommendations.
- `economic`: This boundary is used to define, plan, and analyze a field for business purposes as defined
  by or for the grower. Use examples would include greenhouse gas/sustainability/traceability programs, ownership/splits, and billing.
- `administrative`: This boundary is used to organize data that is defined by some other authority and is generally
  not easy to change. Use examples include government programs, insurance, and legal land description.
- `other`: Any other category of field boundaries.

The categories are based on the [definitions of the AgGateway initiative](https://aggateway.org/Portals/1010/WebSite/About%20Us/FIELD%20BOUNDARY%20FLYER%20122123.pdf?ver=2024-01-03-212959-590).

## Spatial Properties

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

## Determination Properties

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

**determination_method**: Must be one of the following values:

- `manual`: Hand created from imagery, e.g. using a tool to point and click on a map.
- `surveyed`: Determined through a professional land survey measuring the actual distances and angles on the ground.
- `driven`: An operator physically drove (or walked) around the perimeter of the field with a geopositioning device (e.g. GPS) that records the path taken. The operator actively and explicitly selected in the terminal to create a boundary.
- `auto-operation`: Automatically created from operation. Similar to driven but it is an implicit result of normal agricultural operations, so this is usually using the coverage map to determine the boundary.
- `auto-imagery`: Automatically created from aerial or satellite imagery, e.g. using CV or ML techniques.
- `unknown`: The default value. This often means it is defined by some other authority (see `category`) and is likely one of the other methods but there's no knowledge of which exactly.

The determination methods are based on the definitions of the [AgGateway initiative - WG17](https://aggateway.org/).
The specific values have [not been published yet](https://github.com/fiboa/specification/issues/31).
