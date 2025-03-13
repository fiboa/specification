# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- Property `category`
- Property `determination_details`
- Information about the encoding of datatypes at the collection-level

### Changed

- Switched from v0.1.0 to v0.2.0 of the schema language
- Renamed `fiboa_extensions` to `schemas`
- Schemas must be valid HTTP(S) URLs
- GeoParquet: Renamed Parquet metadata key from `fiboa` to `collection`
- GeoJSON: Switched `contentEncoding` for data type `binary` from `binary` to `base64`
- GeoJSON data types: `null` is not allowed any longer, instead omit the property
- GeoJSON FeatureCollection: Collection-level data is provided at the top-level, not in a `fiboa` property

### Removed

- Value `administrative` was removed from `determination_method` in favor of the new property `category`
- `fiboa_version` in favor of adding the schema URL of the specification to `schemas`.
- GeoJSON Feature: `links` property

### Fixed

- Various minor clarifications and editorial enhancements
- Added descriptions to the allowed values for `determination_method`
- GeoJSON: Clarify the encoding of the top-level properties (including `links` and `fiboa`)
- GeoJSON: Clarify the use of RFC 7946
- GeoParquet: Properties that are optional can be omitted if all values are null values
- GeoParquet: Added encoding for bounding boxes and objects
- GeoParquet: Clarified the use of Map and Struct data types

## [v0.2.0] - 2024-04-10

### Added

- `perimeter` property

### Changed

- Migrate schemas to fiboa Schema
- Collections don't need to be STAC Collections (but it's recommended)
- Collections can be included in GeoJSON files
- Collections can be linked to from the GeoJSON files

## [v0.1.0] - 2024-02-28

### Added

- `collection` property
- `determination_method` property
- `determination_datetime` property

### Changed

- Recommend snake_case instead of camcelCase
- `area`: Changed datatype from uint8 to float

### Removed

- Removed `expires` and `datetime`

### Fixed

- Clarified that the id must be unique within the collection
- Clarified `area` and restricted value range
- Clarified the allowed schema formats

## [v0.0.2] - 2024-02-14

- Use .yaml instead of .yml

## [v0.0.1] - 2024-02-14

- First release

[Unreleased]: <https://github.com/fiboa/specification/compare/v0.2.0...main>
[v0.2.0]: <https://github.com/fiboa/specification/compare/v0.1.0...v0.2.0>
[v0.1.0]: <https://github.com/fiboa/specification/compare/v0.0.2...v0.1.0>
[v0.0.2]: <https://github.com/fiboa/specification/compare/v0.0.1...v0.0.2>
[v0.0.1]: <https://github.com/fiboa/specification/tree/v0.0.1>
