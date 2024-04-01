# Mapping of fiboa Data Types to GeoParquet

The following table shows the data types that are used by fiboa in the Property definitions.
It also shows the mapping to the GeoParquet data types.

| fiboa data type                                              | (Geo)Parquet                                                 |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| boolean                                                      | BOOLEAN                                                      |
| int8                                                         | IntType<br />bitWidth: 8<br />isSigned: true<br />(deprecated: INT_8) |
| uint8                                                        | IntType<br />bitWidth: 8<br />isSigned: false<br />(deprecated: UINT_8) |
| int16                                                        | IntType<br />bitWidth: 16<br />isSigned: true<br />(deprecated: INT_16) |
| uint16                                                       | IntType<br />bitWidth: 16<br />isSigned: false<br />(deprecated: UINT_16) |
| int32                                                        | IntType<br />bitWidth: 32<br />isSigned: true<br />(deprecated: INT_32) |
| uint32                                                       | IntType<br />bitWidth: 64<br />isSigned: false<br />(deprecated: UINT_32) |
| int64                                                        | IntType<br />bitWidth: 64<br />isSigned: true<br />(deprecated: INT_64) |
| uint64                                                       | IntType<br />bitWidth: 64<br />isSigned: false<br />(deprecated: UINT_64) |
| float<br />IEEE 32-bit                                       | FLOAT                                                        |
| double<br />IEEE 64-bit                                      | DOUBLE                                                       |
| binary                                                       | BYTE_ARRAY                                                   |
| string<br />charset: UTF-8                                   | STRING (BYTE_ARRAY)                                          |
| array                                                        | LIST                                                         |
| object<br />keys: string<br />values: any                    | MAP                                                          |
| enum<br />string/integer                                     | ENUM (BYTE_ARRAY)                                            |
| date                                                         | DATE (INT32)                                                 |
| date-time<br />with milliseconds<br />timezone: UTC timezone | TimestampType (INT64)<br />isAdjustedToUTC: true<br />unit:  MILLIS<br />(deprecated: TIMESTAMP_MILLIS) |
| geometry                                                     | BYTE_ARRAY<br />encoded as WKB                               |
| bounding-box<br />x and y only, no z                         | [tbd](https://github.com/opengeospatial/geoparquet/pull/191) |
| *required* (not a datatype)                                  | [Nullity](https://parquet.apache.org/docs/file-format/nulls/) |

## Unsupported Data Types

The following data types occur in Parquet, but are not currently supported in fiboa:

- FLOAT16
- FIXED_LEN_BYTE_ARRAY
- UUID (FIXED_LEN_BYTE_ARRAY)
- TimeType (INT32)
  isAdjustedToUTC: true
  unit: MILLIS
  (deprecated: TIME_MILLIS)
- Struct
- JSON

## Potential issues in conversion

- The micro/nanosecond precision of Datetime / Times may got lost
