# Contributing

{% if cookiecutter.project_accepts_issues_prs %}Issues & pull-requests accepted.

- [Create an issue].
- [Fork this repo] and [create a pull-request].{% endif %}

## Install

### Dependencies

- Python {{ cookiecutter.template_python_version }} ([pyenv] recommended)
- [Poetry]

### Installation

```bash
$ poetry install
```

## Usage

### Editor Config

You must configure your editor to:

- Respect an [EditorConfig]
- Enable formating Python with [Black] (on save recommended)
- Enable linting with [pydocstyle] (on save recommended)

<details><summary>See this sample <b>.vscode/settings.json</b></summary>
<p>

```json
{
  "python.formatting.provider": "black",
  "editor.formatOnSave": true,
  "python.linting.pydocstyleEnabled": true
}
```

</p>
</details>

### Run Tests

_Note: Run tests before creating a pull-request_

```bash
$ source .venv/bin/activate
$ pytest
```

<!-- Links -->

[create an issue]: https://docs.github.com/en/github/managing-your-work-on-github/creating-an-issue
[fork this repo]: https://docs.github.com/en/github/getting-started-with-github/fork-a-repo
[create a pull-request]: https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request
[black]: https://github.com/psf/black
[poetry]: https://python-poetry.org/docs/
[pyenv]: https://github.com/pyenv/pyenv
[pydocstyle]: https://pypi.org/project/pydocstyle/
[editorconfig]: https://editorconfig.org/
