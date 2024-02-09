# fiboa Data Types

The following table shows the data types that are used by fiboa in the Property definitions.
It also shows the mapping to the corresponding data types in other popular file formats.

| fiboa data type                                              | (Geo)Parquet                                                 | (Geo)JSON                                                    | FlatGeoBuf                         | Geopackage      | Shapefile          |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ---------------------------------- | --------------- | ------------------ |
| boolean                                                      | BOOLEAN                                                      | boolean                                                      | Bool                               | BOOLEAN         | -                  |
| int8                                                         | IntType<br />bitWidth: 8<br />isSigned: true<br />(deprecated: INT_8) | integer<br />minimum: -128<br />maximum: 127                 | Byte                               | TINYINT         | Short Integer?     |
| uint8                                                        | IntType<br />bitWidth: 8<br />isSigned: false<br />(deprecated: UINT_8) | integer<br />minimum: 0<br />maximum: 255                    | UByte                              | SMALLINT?       | Short Integer?     |
| int16                                                        | IntType<br />bitWidth: 16<br />isSigned: true<br />(deprecated: INT_16) | integer<br />minimum: -32768<br />maximum: 32767             | Short                              | SMALLINT        | Short Integer      |
| uint16                                                       | IntType<br />bitWidth: 16<br />isSigned: false<br />(deprecated: UINT_16) | integer<br />minimum: 0<br />maximum: 65535                  | UShort                             | MEDIUMINT?      | Long Integer?      |
| int32                                                        | IntType<br />bitWidth: 32<br />isSigned: true<br />(deprecated: INT_32) | integer<br />minimum: -2147483648<br />maximum: 2147483647   | Int                                | MEDIUMINT       | Long Integer       |
| uint32                                                       | IntType<br />bitWidth: 64<br />isSigned: false<br />(deprecated: UINT_32) | integer<br />minimum: 0<br />maximum: 4294967295             | UInt                               | INT?            | -                  |
| int64                                                        | IntType<br />bitWidth: 64<br />isSigned: true<br />(deprecated: INT_64) | integer<br />minimum: -9223372036854775808<br />maximum: 9223372036854775807 | Long                               | INT             | -                  |
| uint64                                                       | IntType<br />bitWidth: 64<br />isSigned: false<br />(deprecated: UINT_64) | integer<br />minimum: 0<br />maximum: 18446744073709551615   | ULong                              | -               | -                  |
| float<br />IEEE 32-bit                                       | FLOAT                                                        | number<br />minimum: ?<br />maximum: ?                       | Float                              | FLOAT (REAL)    | Float              |
| double<br />IEEE 64-bit                                      | DOUBLE                                                       | number<br />minimum: ?<br />maximum: ?                       | Double                             | DOUBLE (REAL)   | Double             |
| binary                                                       | BYTE_ARRAY                                                   | string<br />contentEncoding: binary                          | Binary                             | BLOB            | BLOB               |
| string<br />charset: UTF-8                                   | STRING (BYTE_ARRAY)                                          | string                                                       | String                             | TEXT            | Text               |
| array                                                        | LIST                                                         | array                                                        | Json?                              | -               | -                  |
| object<br />keys: string<br />values: any                    | MAP                                                          | object<br />additionalProperties: false                      | Json?                              | -               | -                  |
| enum<br />string/integer                                     | ENUM (BYTE_ARRAY)                                            | string/integer<br />enum                                     | string/integer?                    | TEXT/INT?       | Text/Long Integer? |
| date                                                         | DATE (INT32)                                                 | string<br />format: date                                     | string?                            | DATE (TEXT)     | Date               |
| date-time<br />with milliseconds<br />timezone: UTC timezone | TimestampType (INT64)<br />isAdjustedToUTC: true<br />unit:  MILLIS<br />(deprecated: TIMESTAMP_MILLIS) | string<br />format: date-time<br />pattern: Z$               | DateTime                           | DATETIME (TEXT) | Text?              |
| geometry                                                     | BYTE_ARRAY<br />encoded as WKB                               | [object with schema](https://geojson.org/schema/Geometry.json) | Binary<br />encoded as FlatBuffers | GEOMETRY (BLOB) | Geometry           |
| bounding-box<br />x and y only, no z                         | [tbd](https://github.com/opengeospatial/geoparquet/pull/191) | array<br />minItems: 4<br />maxItems: 4<br />items: number   | Json?                              | ?               | ?                  |
| *optional* (not a datatype)                                  | [Nullity](https://parquet.apache.org/docs/file-format/nulls/) | null                                                         | ?                                  | NULL            | -                  |

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

## Potential issues in conversion

- NaN and +/-Infinity can't be encoded in JSON
- The micro/nanosecond precision of Datetime / Times may got lost
