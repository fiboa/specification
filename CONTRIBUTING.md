# Contributing

Pull Requests are the primary method of contributing to the spec itself,
and everyone is welcome to submit changes.
If the changes can be done as an extension instead of modifying the core files
then that route is recommended first,
and once there is uptake for the extension it will be considered for core.

We consider everyone using the specification to be a 'contributor',
as fiboa is really about the end result of more interoperable data,
not just creating a spec for the sake of it.
So if you want to help then the best thing you can do is make new data set or
build software that uses the spec.
And please do give us feedback.

## Submitting Pull Requests

Any proposed changes to the specification should be done as pull requests.
Creating a Pull Request will show our PR template,
which includes checkbox reminders for a number of things.

- Adding an entry the [CHANGELOG](CHANGELOG.md).
  If the change is more editorial and minor then this is not required,
  but any change to the actual specification must have one.
- Rebase the PR against `main`.
- Highlight if the PR makes breaking changes to the specification.

All pull requests should submit clean markdown, which is checked by the CI.
Please use the commands mentioned below locally before submitting,
to ensure that the checks on the pull request succeed.

All pull requests additionally require a review of two project team members.
Releases are cut from main, see the [process](process.md) document for more details.

## Check files

You'll need to install Python >= 3.9 and pip to setup the test environment.
We use pipenv to execute the tests.

Start with the following command in the folder where this README is located:
`pip install pipenv --user`

Finally, you can run the tests as follows:

- To check the markdown run: `pipenv run test-docs`
- To check the fiboa schema run: `pipenv run test-schema`
- To check the examples run:
  - `pipenv run test-geojson-collection` and `pipenv run test-geojson-features` for GeoJSON
  - `pipenv run test-geoparquet` for GeoParquet
- To create a GeoParquet from the GeoJSON examples: `pipenv run create-geoparquet`
