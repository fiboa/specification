# Validation / fiboa Schema

As fiboa is targeting multiple encodings, there's no single solution for validation.
We must define our own validation vocabulary, based on the [fiboa data types](datatypes.md).

The following keywords are supported:

- `type`: The [fiboa data types](datatypes.md) as a string, **required**.
- `required`: Whether a field is required or not.
  If not required, fields allow a special value such as `null`.
  Defaults to `false`.

Additionally, the following validation vocabulary is defined by JSON Schema:

For strings:

- `format` (values: `email`, `idn-email`, `iri`, `uri`, `uuid`)
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

- `properties` (sub-schemas must be compliant to fiboa Schema)

Note: In fiboa additional properties are disallowed (JSON Schema: `additionalProperties: false`).

fiboa Schema can be translated into JSON Schema.
