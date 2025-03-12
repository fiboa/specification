# Mapping of fiboa Data Types to GeoParquet

The following table shows the data types that are used by fiboa in the Property definitions.
It also shows the mapping to the GeoParquet data types.

| fiboa Schema data type                              | (Geo)Parquet                                                 | Collection-level                |
| --------------------------------------------------- | ------------------------------------------------------------ | ------------------------------- |
| boolean                                             | BOOLEAN                                                      | yes                             |
| int8                                                | IntType<br />bitWidth: 8<br />isSigned: true<br />(deprecated: INT_8) | yes                             |
| uint8                                               | IntType<br />bitWidth: 8<br />isSigned: false<br />(deprecated: UINT_8) | yes                             |
| int16                                               | IntType<br />bitWidth: 16<br />isSigned: true<br />(deprecated: INT_16) | yes                             |
| uint16                                              | IntType<br />bitWidth: 16<br />isSigned: false<br />(deprecated: UINT_16) | yes                             |
| int32                                               | IntType<br />bitWidth: 32<br />isSigned: true<br />(deprecated: INT_32) | yes                             |
| uint32                                              | IntType<br />bitWidth: 64<br />isSigned: false<br />(deprecated: UINT_32) | yes                             |
| int64                                               | IntType<br />bitWidth: 64<br />isSigned: true<br />(deprecated: INT_64) | yes                             |
| uint64                                              | IntType<br />bitWidth: 64<br />isSigned: false<br />(deprecated: UINT_64) | yes                             |
| float<br />IEEE 32-bit                              | FLOAT                                                        | yes                             |
| double<br />IEEE 64-bit                             | DOUBLE                                                       | yes                             |
| binary                                              | BYTE_ARRAY                                                   | as string, base64-encoded       |
| string<br />charset: UTF-8                          | STRING (BYTE_ARRAY)                                          | yes                             |
| array                                               | LIST                                                         | yes                             |
| object<br />keys: string<br />values: any           | STRUCT or MAP (see below)                                    | yes                             |
| date                                                | DATE (INT32)                                                 | as string, compliant to ISO8601 |
| date-time<br />with milliseconds<br />timezone: UTC | TimestampType (INT64)<br />isAdjustedToUTC: true<br />unit:  MILLIS<br />(deprecated: TIMESTAMP_MILLIS) | as string, compliant to ISO8601 |
| geometry                                            | BYTE_ARRAY<br />encoded as WKB                               | no                              |
| bounding-box<br />x and y only, no z                | STRUCT(xmin FLOAT, ymin FLOAT, xmax FLOAT, ymax FLOAT)       | no                              |
| *if a property is not required*                     | [Nullity](https://parquet.apache.org/docs/file-format/nulls/) | yes                             |

The integer data types and the data type string can also be mapped to the ENUM data type in Parquet
if a pre-defined set of values is available.

## Struct vs Map

Parquet has both Map and Struct types. The struct type is similar to a named dictionary while the map type is similar to a list of ordered (key, value) pairs. The main difference is that you need to know up-front the keys for the struct type, while you don't for the map type.

Due to this difference, the **Struct** type can only be used if `additionalProperties` is `false` (the default value) and only `properties` is provided to clearly specify the exact names of the properties.

Any variability in the keys through the use of `additionalProperties` (except for the default `false`) or `patternProperties` requires the use of the **Map** data type. Please note that the order of the Map type is guaranteed to be preserved.

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

- The micro/nanosecond precision of Datetime / Times may get lost
