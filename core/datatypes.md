# fiboa Data Types

The following table shows the data types that are used by fiboa in the Property definitions.
It also shows the mapping to the corresponding data types in other popular file formats.

For more details how the different fiboa data types will be encoded in the different encodings see:
- [GeoJSON](../geojson/datatypes.md)
- [GeoParquet](../geoparquet/datatypes.md)
- [Other](../other/datatypes.md)

| fiboa data type                                              | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| boolean                                                      | a value with only two possible states, e.g. true/false, on/off, or yes/no |
| int8                                                         | integer number without decimal places<br />minimum value: -128<br />maximum value: 127 |
| uint8                                                        | integer number without decimal places<br />minimum value: 0<br />maximum value: 255 |
| int16                                                        | integer number without decimal places<br />minimum value: -32768<br />maximum value: 32767 |
| uint16                                                       | integer number without decimal places<br />minimum value: 0<br />maximum value: 65535 |
| int32                                                        | integer number without decimal places<br />minimum value: -2147483648<br />maximum value: 2147483647 |
| uint32                                                       | integer number without decimal places<br />minimum value: 0<br />maximum value: 4294967295 |
| int64                                                        | integer number without decimal places<br />minimum value: -9223372036854775808<br />maximum value: 9223372036854775807 |
| uint64                                                       | integer number without decimal places<br />minimum value: 0<br />maximum value: 18446744073709551615 |
| float<br />IEEE 32-bit                                       | floating-point number<br />minimum value: ?<br />maximum value: ? |
| double<br />IEEE 64-bit                                      | floating-point number<br />minimum value: ?<br />maximum value: ? |
| binary                                                       | binary data, e.g. an image                                   |
| string<br />charset: UTF-8                                   | texts                                                        |
| array                                                        | a list of values                                             |
| object<br />keys: string<br />values: any                    | key-value-pairs - the keys are always textual and must be known upfront. |
| enum<br />string/integer                                     | integers or texts with a pre-defined list of allowed values  |
| date                                                         | a date consisting of year, month and day, e.g. 2022-07-25    |
| date-time<br />with milliseconds<br />timezone: UTC timezone | a date (year, month, date) and time (hour, minute, second and optionally milliseconds) in the UTC timezone |
| geometry                                                     | A spatial geometry, e.g. a point, line or polygon.           |
| bounding-box<br />x and y only, no z                         | A two-dimensional spatial bounding box                       |
