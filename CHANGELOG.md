# Change Log

All notable changes to this project will be documented in this file.
This project adheres to [Semantic Versioning](http://semver.org/).

### 0.1.8

- Removed testing / support for Python 3.6
- Added testing / support for Python 3.9
- Fixed minor errors in pyproject.toml
- Updated dev dependencies

## 0.1.7

- Fixed a hardcoded package in the issue template
- Fixed a typo in the issue template
- Listed poetry as a dependency in README.md
- Updated ci.yml to work with multiple versions of python
- Updated project slug format to be compatible

## 0.1.6

- Removed `copy_hook` action in **post_gen_project.py** in favor of maintaining two copies (this was just more practical, less magical). This also fixed a bug where variables entered during generation ended up in generated **post_gen_project.py**.
- Simplified **test_bake_project.py**
- Added dynamically generated boilerplate **pyproject.toml**
- Fixed a bug in **workflows/ci.yml** that was installing an incorrect version of Poetry

## 0.1.5

- Added simple GitHub workflow to run `pytest`

## 0.1.4

- Simplified **cookiecutter.json** options
- Added a code of conduct to repo
- Added option to generate a code of conduct via [GitHub API]

## 0.1.3

- Added missing GitHub Issue & Pull Requests tempaltes to generated template

## 0.1.2

- Fixed bug where generated **cookiecutter.json**, **project_slug** was getting set to what was entered during initial generation

## 0.1.1

- Fixed bug with GitHub Issue & Pull Request templates
- Added "No License" option to **project_license** in **cookiecutter.json**

## 0.1.0

- Initial build

<!-- Links -->

[github api]: "https://docs.github.com/en/rest"
