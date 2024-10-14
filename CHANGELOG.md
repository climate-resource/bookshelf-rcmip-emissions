# Changelog

Versions follow [Semantic Versioning](https://semver.org/) (`<major>.<minor>.<patch>`).

Backward incompatible (breaking) changes will only be introduced in major versions
with advance notice in the **Deprecations** section of releases.

<!--
You should *NOT* be adding new changelog entries to this file,
this file is managed by towncrier.
See `changelog/README.md`.

You *may* edit previous changelogs to fix problems like typo corrections or such.
To add a new changelog entry, please see
`changelog/README.md`
and https://pip.pypa.io/en/latest/development/contributing/#news-entries,
noting that we use the `changelog` directory instead of news,
markdown instead of restructured text and use slightly different categories
from the examples given in that link.
-->

<!-- towncrier release notes start -->

## RCMIP Emissions v0.1.1 (2024-10-14)

### Bug Fixes

- Include tarball of built data as part of a release ([#4](https://github.com/climate-resource/bookshelf-rcmip-emissions/pull/4))


## RCMIP Emissions v0.1.0 (2024-10-14)

### Improvements

- Adds a dependency on the bookshelf-producer package. ([#1](https://github.com/climate-resource/bookshelf-rcmip-emissions/pull/1))
- Add a basic CI to verify the notebooks are working as expected ([#2](https://github.com/climate-resource/bookshelf-rcmip-emissions/pull/2))
- Use get-version script instead of a sed one-liner ([#3](https://github.com/climate-resource/bookshelf-rcmip-emissions/pull/3))
