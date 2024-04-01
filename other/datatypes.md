# fiboa Data Types

The following table shows the data types that are used by fiboa in the Property definitions.
It explores the mapping to the corresponding data types in other file formats.

| fiboa data type                                              | FlatGeoBuf                         | Geopackage      | Shapefile          |
| ------------------------------------------------------------ | ---------------------------------- | --------------- | ------------------ |
| boolean                                                      | Bool                               | BOOLEAN         | -                  |
| int8                                                         | Byte                               | TINYINT         | Short Integer?     |
| uint8                                                        | UByte                              | SMALLINT?       | Short Integer?     |
| int16                                                        | Short                              | SMALLINT        | Short Integer      |
| uint16                                                       | UShort                             | MEDIUMINT?      | Long Integer?      |
| int32                                                        | Int                                | MEDIUMINT       | Long Integer       |
| uint32                                                       | UInt                               | INT?            | -                  |
| int64                                                        | Long                               | INT             | -                  |
| uint64                                                       | ULong                              | -               | -                  |
| float<br />IEEE 32-bit                                       | Float                              | FLOAT (REAL)    | Float              |
| double<br />IEEE 64-bit                                      | Double                             | DOUBLE (REAL)   | Double             |
| binary                                                       | Binary                             | BLOB            | BLOB               |
| string<br />charset: UTF-8                                   | String                             | TEXT            | Text               |
| array                                                        | Json?                              | -               | -                  |
| object<br />keys: string<br />values: any                    | Json?                              | -               | -                  |
| enum<br />string/integer                                     | string/integer?                    | TEXT/INT?       | Text/Long Integer? |
| date                                                         | string?                            | DATE (TEXT)     | Date               |
| date-time<br />with milliseconds<br />timezone: UTC timezone | DateTime                           | DATETIME (TEXT) | Text?              |
| geometry                                                     | Binary<br />encoded as FlatBuffers | GEOMETRY (BLOB) | Geometry           |
| bounding-box<br />x and y only, no z                         | Json?                              | ?               | ?                  |
| *required* (not a datatype)                                  | ?                                  | NULL            | -                  |

## Unsupported Data Types

The following data types occur e.g. in Parquet, but are not currently supported in fiboa.

| (Geo)Parquet                                                 | (Geo)JSON                                                    | FlatGeoBuf | Geopackage | Shapefile |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ---------- | ---------- | --------- |
| FLOAT16                                                      | number<br />minimum: ?<br />maximum: ?                       | Float?     | FLOAT?     | Float?    |
| FIXED_LEN_BYTE_ARRAY                                         | string<br />contentEncoding: binary<br />minLength and maxLength | Binary?    | BLOB?      | BLOB?     |
| UUID (FIXED_LEN_BYTE_ARRAY)                                  | string<br />format: uuid                                     | Binary?    | BLOB?      | ?         |
| TimeType (INT32)<br />isAdjustedToUTC: true<br />unit: MILLIS<br />(deprecated: TIME_MILLIS) | string<br />format: time<br />pattern: Z$                    | ?          | TEXT?      | Text?     |
| Struct                                                       | object                                                       | Json?      | -          | -         |
| JSON                                                         | any                                                          | Json       | -          | -         |

Additionally, Shapefile has the big drawback that the field name limit is 10 characters.
As such it doesn't work well with fiboa and its extension mechanism.

## Potential issues in conversion

- The micro/nanosecond precision of Datetime / Times may got lost
