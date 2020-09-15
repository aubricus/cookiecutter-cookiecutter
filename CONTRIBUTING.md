# Contributing

Issues & pull-requests accepted.

- [Create an issue].
- [Fork this repo] and [create a pull-request].

## Install

### Dependencies

- Python 3.6 ([pyenv] recommended)
- [Virtualenv]
- [Poetry]

### Installation

```bash
$ poetry install
$ source .venv/bin/activate
```

## Usage

### Editor Settings

You must configure your editor to:

- Select `python` from local .venv folder
- Respect an [EditorConfig]
- Enable formating Python with [Black] (on save recommended)
- Enable linting with [pydocstyle] (on save recommended)

<details><summary>See this sample <b>.vscode/settings.json</b></summary>
<p>

```json
{
  "python.pythonPath": ".venv/bin/python",
  "python.formatting.provider": "black",
  "editor.formatOnSave": true,
  "python.linting.pydocstyleEnabled": true
}
```

Note: [EditorConfig] is supported by a [VSCode EditorConfig Extension]

</p>
</details>

### Run Tests

_Note: Run tests before creating a pull-request_

```bash
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
[virtualenv]: https://virtualenv.pypa.io/en/latest/
[vscode editorconfig extension]: https://github.com/editorconfig/editorconfig-vscode
