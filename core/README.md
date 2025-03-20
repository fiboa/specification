# Core Specification <!-- omit in toc -->

This specification describes the core data and metadata properties that describe a fiboa Feature.
The specification doesn't distinguish between collection-level and feature-level properties,
common definitions are shared across these levels.

- A Collection refers to a group of one or more features.
- A Feature is a single field geometry with additional properties.

- **Schema:** <https://fiboa.github.io/specification/v0.3.0/schema.yaml>

## Table of Contents <!-- omit in toc -->

- [General Properties](#general-properties)
  - [schemas](#schemas)
  - [id](#id)
  - [collection](#collection)
  - [category](#category)
- [Spatial Properties](#spatial-properties)
  - [area / perimeter](#area--perimeter)
- [Determination Properties](#determination-properties)
  - [determination\_datetime](#determination_datetime)
  - [determination\_method](#determination_method)
- [Schema Language](#schema-language)

## General Properties

| Property Name | Data Type                       | Description |
| ------------- | ------------------------------- | ----------- |
| schemas       | object\<string, array\<string>> | **REQUIRED.** A list of schemas the collection implements. |
| id            | string                          | **REQUIRED.** An identifier for the field. |
| collection    | string                          | **REQUIRED.** The identifier of the collection. |
| category      | array\<string>                  | A set of categories the field boundary belongs to. |

### schemas

The schemas the collection implements.
Each schema must be a valid HTTP(S) URLs to an existing YAML files compliant to fiboa Schema.
The schema for this specification (see above) is required to be provided.

Each `collection` must have a single set of applicable schemas.
The key of the dictionary must be equal to the value provided for the `collection` property.

The schema URI for fiboa that is listed above is required to be present.

**Example for `schemas`:**

This describes two collections `abc` and `xyz`.

```json
{
  "abc": [
    "https://fiboa.github.io/specification/v0.3.0/schema.yaml"
  ],
  "xyz": [
    "https://fiboa.github.io/specification/v0.3.0/schema.yaml",
    "https://fiboa.github.io/crop-extension/v0.1.0/schema.yaml",
  ]
}
```

### id

It must be unique per collection, i.e. `collection` and `id` form a unique identifier.

### collection

A collection is a group of one or more features with a unique identifier, stored in the `collection` property.

Encodings may support to store properties that consists of the same value across all features at the collection-level.
This de-duplicates data for more efficient resource usage, but only applies if more than two features are available for the collection.
The specific location and behaviour of collection-level data is specified in the encoding-specific specifications.

**Example:**

You have two different field boundary datasets named `abc` (CC-0 licensed) and `xyz` (CC-BY-4.0 licensed).
If you store the datasets separately, you can store the license in the collection-level data
as the value for the property is the same for all features.
Once you merged the two datasets, you must ensure that a unique identifier for the collection is provieded
(here: `abc` and `xyz`) so that IDs are unique.
Additionally, you have to add the license property on the feature-level as the licenses are now twofold.

### category

Choose any (unique) combination of the following values:

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

### area / perimeter

These are derived attributes from the geometry itself,
and must match the geometry's area/perimeter. If they do not match then the
geometry should be considered canonical.
Validators may flag the value as invalid if it exceeds a certain threshold.

## Determination Properties

| Property Name          | Data Type | Description |
| ---------------------- | --------- | ----------- |
| determination_method   | string    | The boundary creation method, one of the values below. |
| determination_datetime | datetime  | The last timestamp at which the field did exist and was observed. |
| determination_details  | string    | Further details about the determination, especially the methodology. |

### determination_datetime

The last timestamp at which the field did exist and was observed, provided in the UTC timezone.

In case the source of the information is an interval or a set of timestamps, use the end.
For example, for ML you'd use the timestamp of the last image and not the
timestamp of the actual execution.

> [!NOTE]  
> We define more temporal properties in the
> [timestamps extension](https://github.com/fiboa/timestamps).

### determination_method

The determination method must be one of the following values:

- `manual`: Hand created from imagery, e.g. using a tool to point and click on a map.
- `surveyed`: Determined through a professional land survey measuring the actual distances and angles on the ground.
- `driven`: An operator physically drove (or walked) around the perimeter of the field with a geopositioning device (e.g. GPS) that records the path taken. The operator actively and explicitly selected in the terminal to create a boundary.
- `auto-operation`: Automatically created from operation. Similar to driven but it is an implicit result of normal agricultural operations, so this is usually using the coverage map to determine the boundary.
- `auto-imagery`: Automatically created from aerial or satellite imagery, e.g. using CV or ML techniques.
- `unknown`: The default value. This often means it is defined by some other authority (see `category`) and is likely one of the other methods but there's no knowledge of which exactly.

The determination methods are based on the definitions of the [AgGateway initiative - WG17](https://aggateway.org/).
The specific values have [not been published yet](https://github.com/fiboa/specification/issues/31).

## Schema Language

The schema language used for fiboa is [fiboa Schema](https://github.com/fiboa/schema), version 0.2.0.

The data types in the tables above are defined in the document
[Data Types](https://github.com/fiboa/schema/blob/v0.2.0/datatypes.md).

fiboa Schema defines a (limited) set of data types and a
[vocabulary](https://github.com/fiboa/schema/blob/v0.2.0/README.md#vocabulary)
to express additional constraints for these data types.
This allows to define a clear mapping between the core specification and its encodings.
