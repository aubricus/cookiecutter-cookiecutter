# CookieCutter CookieCutter

[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme) [![code style black](https://img.shields.io/badge/code%20style-black-%23000000)](https://github.com/psf/black) [![License MIT](https://img.shields.io/github/license/aubricus/cookiecutter-cookiecutter?v=1)](./LICENSE)

_A [CookieCutter] template to generate [CookieCutter] templates._

## Background

This is inspired by [eviweb/cookiecutter-template] ([v0.1.1](https://github.com/eviweb/cookiecutter-template/releases/tag/v0.1.1)).

## Install

### Dependencies

- Python 3.6 ([pyenv] recommended)
- [CookieCutter]

### Installation

```bash
$ pip install -U cookiecutter
```

## Usage

```bash
$ cookiecutter gh:aubricus/cookiecutter-cookiecutter
```

## Features

This [CookieCutter] template generates a [CookieCutter] template...

With the following defaults:

- [Standard Readme] formatted README.md
- Lightweight CHANGELOG.md, CONTRIBUTING.md, and GitHub issue & pull-request templates
- LICENSE file generated with [GitHub API]
- [Poetry] for virtual env and dependency management
- [pytest] test suite (with [pytest-cookies])
- [EditorConfig], [Black], & [pydocstyle] formatting & linting
- Lightweight defaults for the generated `{{cookiecutter.project_slug}}` directory:
  - [Standard Readme] formatted README.md
  - Lightweight CHANGELOG.md, CONTRIBUTING.md

With the following features:

- Declaritively tell [CookieCutter] to ignore files by appending a `.donotrender` extension

## Support

- Last tested under Python 3.6.9 on MacOS 10.15.5 (manual & automated testing locally)
- Linux & Windows (not tested)

## Maintainers

- [aubricus]

## Attribution

This template was generated with [cookiecutter/cookiecutter] and [eviweb/cookiecutter-template]!

## Contributing

Issues & pull-requets accepted. See the [CONTRIBUTING.md]

_Small note: If editing the [README.md], please conform to the [standard-readme specification]._

## License

[MIT] &copy; Aubrey Taylor 2020

<!-- Links -->

[poetry]: https://github.com/sdispater/poetry
[setuptools]: https://setuptools.readthedocs.io/en/latest/
[twine]: https://github.com/pypa/twine
[pytest]: https://docs.pytest.org/en/latest/
[tox]: https://tox.readthedocs.io/en/latest/
[standard readme]: https://github.com/RichardLitt/standard-readme
[pdoc]: https://pdoc3.github.io/pdoc/
[github pages]: https://pages.github.com/
[black]: https://github.com/psf/black
[pyenv]: https://github.com/pyenv/pyenv
[gitignore.io]: http://gitignore.io/
[github api]: https://developer.github.com/v3/licenses/
[aubricus]: https://github.com/aubricus
[cookiecutter/cookiecutter]: https://github.com/cookiecutter/cookiecutter
[eviweb/cookiecutter-template]: https://github.com/eviweb/cookiecutter-template
[standard-readme specification]: https://github.com/RichardLitt/standard-readme
[mit]: ./LICENSE
[readme.md]: ./README.md
[travis ci]: https://travis-ci.org/
[cookiecutter]: https://github.com/cookiecutter/cookiecutter
[poetry]: https://python-poetry.org/docs/
[contributing.md]: ./CONTRIBUTING.md
[pydocstyle]: https://www.pydocstyle.org/en/stable/
[editorconfig]: https://editorconfig.org/
[pytest-cookies]: https://pytest-cookies.readthedocs.io/en/latest/