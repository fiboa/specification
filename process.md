# fiboa Development & Release Process

## Development Process

The fiboa specification is under active development.
The goal is to get to a small, flexible stable release that can be extended in a variety of ways.

The [released versions](https://github.com/fiboa/specification/releases) aims to always be stable,
meaning that all the pieces of the specification are consistent and well explained,
and all the examples are consistent with the specification.
The `main` branch is a place of active development, where a new change in one part
of the spec might not yet be fully updated everywhere else.
The team uses the [issue tracker](https://github.com/fiboa/specification/issues)
to identify and track all that will be done for a release.

Any changes to the spec must be proposed as pull requests.
Anyone is welcome and encouraged to bring ideas and improvements to the issue tracker
or (ideally) as pull requests.
To merge a new pull request the work must be reviewed by at least two members of
the past contributors that have write access to the repository.
It also must pass the Continuous Integration (CI) testing, which checks all markdown and example
files for proper formatting, and also validates all examples against the schemas.

Check the [contributing guide](CONTRIBUTING.md) for more details.

## Release Process

To release a new version of the STAC spec the following list of tasks must be done. 

- **Update Issue Tracker**:
  Each release has a corresponding [milestone](https://github.com/fiboa/specification/milestones),
  and before a release is done all open issues that are filed against it should be reviewed.
  All issues do not need to be completed, but the core release team should all review the issues
  to make sure that the critical ones for the release have been addressed.
  Issues that aren't seen as essential should be moved to future releases,
  so that there are no open issues against the milestone.
- **Agreement from the Project Team**:
  The project team should meet and decided that the release is ready.
  This should include review of the issues, as well as looking at the spec holistically,
  to make sure the new changes keep with a coherent whole.
- **Final Spec Read Through**:
  There should be a final read through of the core specification to make sure
  it makes sense and there are no typos, errors, etc.
- **Update the version numbers**:
  There are several places in the spec that use the version number in text or a link.
  These include the markdown files and the JSON schemas.
  Right now the best thing to do is just a search & replace for the last version number.
- **Update the Changelog**:
  The [Changelog](CHANGELOG.md) should be reviewed to make sure it includes all
  major improvements in the release.
  And anything in 'Unreleased' section should move to the version of the spec to be released.
- **Release on Github**:
  The final step to create the release is to add a new 'release' on
  <https://github.com/fiboa/specification/releases>.
  This should use a tag like the others, with a 'v' prefix and then the release number, like v1.0.2.
  The changelog should be copied over to be the release notes, and then also include a link to 
  the full milestone of everything closed in the issue tracker.
- **Promote the release**:
  A blog post and social media posts should be composed and sent out to post / promote it.
