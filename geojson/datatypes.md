# Mapping of fiboa Data Types to GeoJSON

The following table shows the data types that are used by fiboa in the Property definitions.
It also shows the mapping to the GeoJSON data types.

| fiboa data type                                     | (Geo)JSON                                                    | Collection-level |
| --------------------------------------------------- | ------------------------------------------------------------ | ---------------- |
| boolean                                             | boolean                                                      | yes              |
| int8                                                | integer<br />minimum: -128<br />maximum: 127                 | yes              |
| uint8                                               | integer<br />minimum: 0<br />maximum: 255                    | yes              |
| int16                                               | integer<br />minimum: -32768<br />maximum: 32767             | yes              |
| uint16                                              | integer<br />minimum: 0<br />maximum: 65535                  | yes              |
| int32                                               | integer<br />minimum: -2147483648<br />maximum: 2147483647   | yes              |
| uint32                                              | integer<br />minimum: 0<br />maximum: 4294967295             | yes              |
| int64                                               | integer<br />minimum: -9223372036854775808<br />maximum: 9223372036854775807 | yes |
| uint64                                              | integer<br />minimum: 0<br />maximum: 18446744073709551615   | yes              |
| float<br />IEEE 32-bit                              | number<br />minimum: ?<br />maximum: ?                       | yes              |
| double<br />IEEE 64-bit                             | number<br />minimum: ?<br />maximum: ?                       | yes              |
| binary                                              | string<br />contentEncoding: base64                          | yes              |
| string<br />charset: UTF-8                          | string                                                       | yes              |
| array                                               | array                                                        | yes              |
| object<br />keys: string<br />values: any           | object<br />additionalProperties: false                      | yes              |
| date                                                | string<br />format: date                                     | yes              |
| date-time<br />with milliseconds<br />timezone: UTC | string<br />format: date-time<br />pattern: Z$               | yes              |
| geometry                                            | [object with schema](https://geojson.org/schema/Geometry.json) | no             |
| bounding-box<br />x and y only, no z                | array<br />minItems: 4<br />maxItems: 4<br />items: number   | no               |

## Missing values

For optional properties, values might be missing.
This is expressed by omitting the JSON property.
The value `null` is not allowed.

## Potential issues in conversion

- NaN and +/-Infinity can't be encoded in JSON
