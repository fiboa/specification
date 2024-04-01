# Mapping of fiboa Data Types to GeoJSON

The following table shows the data types that are used by fiboa in the Property definitions.
It also shows the mapping to the GeoJSON data types.

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
| object<br />keys: string<br />values: any                    | object<br />additionalProperties: false                      |
| enum<br />string/integer                                     | string/integer<br />enum                                     |
| date                                                         | string<br />format: date                                     |
| date-time<br />with milliseconds<br />timezone: UTC timezone | string<br />format: date-time<br />pattern: Z$               |
| geometry                                                     | [object with schema](https://geojson.org/schema/Geometry.json) |
| bounding-box<br />x and y only, no z                         | array<br />minItems: 4<br />maxItems: 4<br />items: number   |
| *required* (not a datatype)                                  | null                                                         |

## Potential issues in conversion

- NaN and +/-Infinity can't be encoded in JSON
