# Mapping of fiboa Data Types to FlatGeobuf

The following table shows the data types that are used by fiboa in the Property definitions.
It also shows the mapping to the [FlatGeobuf data types](https://github.com/flatgeobuf/flatgeobuf/blob/ee7c8f5f45c67dd4a84a51fef518dfebc3e19d0a/src/fbs/header.fbs#L26-L42).

| fiboa Schema data type                              | FlatGeobuf                                                 |
| --------------------------------------------------- | ------------------------------------------------------------ |
| boolean                                             | Bool                                                       |
| int8                                                | Byte                                                       |
| uint8                                               | UByte |
| int16                                               | Short |
| uint16                                              | UShort |
| int32                                               | Int |
| uint32                                              | UInt |
| int64                                               | Long |
| uint64                                              | ULong |
| float<br />IEEE 32-bit                              | Float                                                        |
| double<br />IEEE 64-bit                             | Double                                                       |
| binary                                              | Binary                                                   |
| string<br />charset: UTF-8                          | String                                          |
| array                                               | Json Array                                                         |
| object<br />keys: string<br />values: any           | Json Object                                                 |
| date                                                | DateTime (ISO 8601 date)                                                 |
| date-time<br />with milliseconds<br />timezone: UTC | DateTime (ISO 8601 date time) |
| geometry                                            | [Geometry](https://github.com/flatgeobuf/flatgeobuf/blob/ee7c8f5f45c67dd4a84a51fef518dfebc3e19d0a/src/fbs/feature.fbs#L5-L14)                               |
| bounding-box<br />x and y only, no z                | Json <br>Bounds Array [minX, minY, maxX, maxY]|

## Potential issues in conversion

TBD
