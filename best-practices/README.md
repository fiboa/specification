# Best Practices

> [!NOTE]  
> We are in an early stage. More best practices will evolve over time.

## Casing

All properties should be using snake case.
For example a field for a land-use class should be named `landuse_class` instead of `landuseClass`.

## Extension prefixes

All properties in an extensions should have a common prefix.
Extensions commonly use the colon (`:`) as separator between prefix and property name, e.g. `crop:name`.
A single underscore (`_`) should be avoided to avoid conflicts with other property names (see [Casing](#casing)).
Nevertheless, the separator can be chosen freely by extension authors.
