# fiboa Data Types

The following table shows the data types that are used by fiboa in the Property definitions.
It also shows the mapping to the corresponding data types in other popular file formats.

| fiboa data type                                              | (Geo)JSON                                                    |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| boolean                                                      | boolean                                                      |
| int8                                                         | integer<br />minimum: -128<br />maximum: 127                 |
| uint8                                                        | integer<br />minimum: 0<br />maximum: 255                    |
| int16                                                        | integer<br />minimum: -32768<br />maximum: 32767             |
| uint16                                                       | integer<br />minimum: 0<br />maximum: 65535                  |
| int32                                                        | integer<br />minimum: -2147483648<br />maximum: 2147483647   |
| uint32                                                       | integer<br />minimum: 0<br />maximum: 4294967295             |
| int64                                                        | integer<br />minimum: -9223372036854775808<br />maximum: 9223372036854775807 |
| uint64                                                       | integer<br />minimum: 0<br />maximum: 18446744073709551615   |
| float<br />IEEE 32-bit                                       | number<br />minimum: ?<br />maximum: ?                       |
| double<br />IEEE 64-bit                                      | number<br />minimum: ?<br />maximum: ?                       |
| binary                                                       | string<br />contentEncoding: binary                          |
| string<br />charset: UTF-8                                   | string                                                       |
| array                                                        | array                                                        |
| object<br />keys: string<br />values: any                    | object                                                       |
| enum<br />string/integer                                     | string/integer<br />enum                                     |
| date                                                         | string<br />format: date                                     |
| date-time<br />with milliseconds<br />timezone: UTC timezone | string<br />format: date-time<br />pattern: Z$               |
| geometry                                                     | [object with schema](https://geojson.org/schema/Geometry.json) but not null |
| bounding-box<br />x and y only, no z                         | array<br />minItems: 4<br />maxItems: 4<br />items: number   |
| *optional* (not a datatype)                                  | null                                                         |

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
