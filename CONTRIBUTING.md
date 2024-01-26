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

You'll need to install [nodejs and npm](https://nodejs.org/en/download/) to run the tests.
Alternatively, you can also use [yarn](https://yarnpkg.com/) instead of npm.
In this case replace all occurrences of `npm` with `yarn` below.

Afterwards, navigate to the root of the specification repository.
Now, install the required test software: `npm install`

Finally, you can run all tests or subset of them:

- To run all tests: `npm test`
- To check the markdown run: `npm run check-docs`
- To check the examples run: `npm run check-examples`
