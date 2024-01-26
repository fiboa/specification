# Data and Metadata Specification

## Properties

### General

| Property Name    | Data Type       | Description |
| ---------------- | --------------- | ----------- |
| fiboa_version    | string          | **REQUIRED.** Version number of the fiboa specification this entity implements. |
| fiboa_extensions | \[string]       | A list of URIs to extensions this entity implements. |
| id               | string          | **REQUIRED.** A unique identifier for the field. |
| license          | string          | **REQUIRED.** License of the data as SPDX identifier or `other`. If set to `other`, a link to the license must be provided with the relation type `license`. |
| links            | \[Link Object\] | A list of links to other resources. |

### Spatial

| Property Name | Data Type | Description |
| ------------- | --------- | ----------- |
| geometry      | object    | **REQUIRED.** A geometry that reflects the footprint of the field, usually a Polygon. Default CRS is WGS84. |
| bbox          | \[number] | **REQUIRED.** The bounding box of the field. |
| area          | number    | Area of the field, in ha and > 0. |

**bbox:** The value of the bbox member MUST be an array of length 2*n where n is the number of
dimensions represented in the contained geometries, with all axes of the most southwesterly point
followed by all axes of the more northeasterly point.

### Temporal

| Property Name | Data Type | Description |
| ------------- | --------- | ----------- |
| datetime      | string    | The data is valid since the given date and time (inclusive), in UTC and formatted according to RFC 3339, section 5.6. |
| expires       | string    | The data is valid until the given date and time (exclusive), in UTC and formatted according to RFC 3339, section 5.6. |

### Other Data Types

#### Link Object

This object describes a relationship with another entity.
Data providers are advised to be liberal with links.

| Field Name | Type   | Description |
| ---------- | ------ | ----------- |
| href       | string | **REQUIRED.** The actual link in the format of an URL. Relative and absolute links are both allowed. |
| rel        | string | **REQUIRED.** Relationship between the current document and the linked document. See chapter [Relation Types](#relation-types) for more information. |
| type       | string | IANA media type of the referenced entity. |
| title      | string | A human readable title to be used in rendered displays of the link. |

##### Relation Types

Where possible it is recommended to use the official
[IANA Link Relation Types](https://www.iana.org/assignments/link-relations/link-relations.xhtml).

| Type    | Description |
| ------- | ----------- |
| self    | STRONGLY RECOMMENDED. *Absolute* URL to the location that the file can be found online, if available. This is particularly useful when in a download package that includes metadata, so that the downstream user can know where the data has come from. |
| license | The license URL(s) for the data SHOULD be specified if the `license` field is set to `other`. If there is no public license URL available, it is RECOMMENDED to put the license text in a separate file and link to this file. |
