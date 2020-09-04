# {{ cookiecutter.project_name }}

[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme) [![code style black](https://img.shields.io/badge/code%20style-black-%23000000)](https://github.com/psf/black) [![License {{ cookiecutter.project_license }}](https://img.shields.io/github/license/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }})](./LICENSE)

{% if cookiecutter.project_summary %}_{{ cookiecutter.project_summary }}_{% endif %}

{% if cookiecutter.project_background %}## Background

{{ cookiecutter.project_background }}{% endif %}

## Install

### Dependencies

- {{ cookiecutter.template_python_version }} ([pyenv] recommended)
- [CookieCutter]

### Installation

```bash
$ pip install -U cookiecutter
```

## Usage

```bash
$ cookiecutter gh:{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}
```

## Features

This [CookieCutter] generates a project with...

With the following defaults:

- [Standard Readme] formatted README.md
- Lightweight CHANGELOG.md, CONTRIBUTING.md
- LICENSE file generated with [GitHub API]

With the following features:

- Declaritively tell [CookieCutter] to ignore files by appending a `.donotrender` extension

## Support

- _TODO: Update_

## Maintainers

- [{{ cookiecutter.github_username }}](https://github.com/{{ cookiecutter.github_username }})

## Attribution

This template was generated with [cookiecutter/cookiecutter] and [aubricus/cookiecutter-cookiecutter]!

## Contributing

{% if cookiecutter.project_accepts_issues_prs %}Issues & pull-requets accepted. See the [CONTRIBUTING.md]{% endif %}

_Small note: If editing the [README.md], please conform to the [standard-readme specification]._

## License

[{{ cookiecutter.project_license }}](./LICENSE) &copy; {{ cookiecutter.full_name }} 2020

<!-- Links -->

[setuptools]: https://setuptools.readthedocs.io/en/latest/
[twine]: https://github.com/pypa/twine
[pytest]: https://docs.pytest.org/en/latest/
[tox]: https://tox.readthedocs.io/en/latest/
[standard readme]: https://github.com/RichardLitt/standard-readme
[black]: https://github.com/psf/black
[pyenv]: https://github.com/pyenv/pyenv
[github api]: https://developer.github.com/v3/licenses/
[cookiecutter]: https://github.com/cookiecutter/cookiecutter
[cookiecutter/cookiecutter]: https://github.com/cookiecutter/cookiecutter
[aubricus/cookiecutter-cookiecutter]: https://github.com/aubricus/cookiecutter-cookiecutter
[standard-readme specification]: https://github.com/RichardLitt/standard-readme
[readme.md]: ./README.md
[poetry]: https://python-poetry.org/docs/
[contributing.md]: ./CONTRIBUTING.md
[pydocstyle]: https://www.pydocstyle.org/en/stable/
[editorconfig]: https://editorconfig.org/
