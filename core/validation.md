# Validation / fiboa Schema

As fiboa is targeting multiple encodings, there's no single solution for validation.
We must define our own validation vocabulary, based on the [fiboa data types](datatypes.md).

The following keywords are supported:

- `type`: The [fiboa data types](datatypes.md) as a string, **required**.
- `optional`: Defines whether having a value is optional,
  which usually means null or a similar value is allowed to be set

Additionally, the following validation vocabulary is defined by JSON Schema:

For strings:

- `pattern`
- `minLength`
- `maxLength`
- `enum`: An array of allowed strings

For numerical data types:

- `minimum`
- `maximum`
- `exclusiveMinimum`
- `exclusiveMaximum`
- `enum`: An array of allowed **integers**.

For arrays:

- `items` (object only, sub-schema must be compliant to fiboa Schema)
- `minItems`
- `maxItems`
- `uniqueItems`

For objects:

- `required`
- `properties` (sub-schemas must be compliant to fiboa Schema)

Note: In fiboa additional properties are disallowed (JSON Schema: `additionalProperties: false`).

fiboa Schema can be translated into JSON Schema.
