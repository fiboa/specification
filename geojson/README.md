# GeoJSON Encoding Specification

- **[Examples](examples/):**
  1. [as a FeatureCollection](examples/featurecollection/features.json)
  2. [as individual Features with a dedicated STAC Collection](examples/individual-features/)
- **[Datatype mapping](datatypes.md)**

**NOTE: The GeoJSON encoding is still work in progress. Feedback is always welcome!**

## Collection

A [fiboa Collection](../core/README.md#collection) must be provided as a JSON object, either
1. embedded into the GeoJSON in a top-level property named `fiboa` (example 1), or
2. separately as a JSON file that is linked to from the GeoJSON (example 2).

All features in a FeatureCollection must be fiboa-compliant.

## Feature Properties

Feature-level data and metadata refers to a single GeoJSON Feature.

The following properties are provided in the GeoJSON document at the top-level:
- id
- geometry
- bbox

All other properties reside in the GeoJSON `properties`.
