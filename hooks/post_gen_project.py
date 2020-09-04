"""Cookiecutter post_gen_project hook.

See: https://cookiecutter.readthedocs.io/en/1.7.2/advanced/hooks.html
"""

import os
import json
import urllib
import shutil
import fileinput
from urllib import request
from urllib.request import Request
from datetime import date
from pathlib import Path


def get_license():
    """Get the selected license from GitHub API."""
    full_name = "{{ cookiecutter.full_name }}"
    email = "{{ cookiecutter.email }}"
    project_license = "{{ cookiecutter.project_license}}".lower()
    base_url = "https://api.github.com/licenses"
    url = f"{base_url}/{project_license}"
    headers = {"Accept": "application/vnd.github.v3+json"}

    try:
        req = Request(url, headers=headers)
    except urllib.error.HTTPError as e:
        print(f"Request failed: {e}")
        sys.exit(1)

    res = request.urlopen(req)
    data = json.loads(res.read())

    if project_license == "mit":
        write_license_mit(data["body"], full_name, email)
    elif project_license == "apache-2.0":
        write_license_apache2(data["body"], full_name, email)
    else:
        write_license(data["body"])


def write_license(content):
    """Write content to a LICENSE file."""
    with open("LICENSE", "w") as f:
        f.write(content)


def write_license_mit(content, full_name, email):
    """Write an MIT LICENSE."""
    year = date.today().year
    content = content.replace("[year]", str(year)).replace(
        "[fullname]", f"{full_name} <{email}>"
    )
    write_license(content)


def write_license_apache2(content, full_name, email):
    """Write an Apache 2.0 LICENSE."""
    year = date.today().year
    content = content.replace("[yyyy]", str(year)).replace(
        "[name of copyright owner]", f"{full_name} <{email}>"
    )
    write_license(content)


def remove_donotrender_ext():
    """Remove .donotrenderext from all files.

    This template uses a custom `.donotrender` extension
    which is set as part of the _copy_without_render config
    in [cookiecutter.json](./cookiecutter.json).

    This convention was created to keep config simple
    and create a more declarative approach for telling
    cookiecutter to ignore files.

    This function removes that extension to restore
    the original filename/extension.
    """
    ext = "donotrender"
    paths = Path.cwd().rglob(f"*.{ext}")
    for p in paths:
        p.replace(p.with_suffix(""))


# [Remove]
# NOTE: The above directive is used to remove this section during copy_hook
def copy_hook():
    """Copy this repo's post_gen_project hook to the template."""
    src = Path(__file__)
    dest = Path.cwd().joinpath("hooks/post_gen_project.py")

    try:
        os.makedirs(str(dest.parent))
        shutil.copy(str(src), str(dest))
    except FileExistsError:
        shutil.copy(str(src), str(dest))

    _do_post_copy_remove(dest)


def _do_post_copy_remove(file_path):
    remove_token = "# [Remove]"
    remove_closing_token = "# [End Remove]"
    skip_line = False
    with fileinput.FileInput(str(file_path), inplace=True) as f:
        for line in f:
            line = line.strip("\n")
            if line.strip() == remove_token:
                skip_line = True

            if not skip_line:
                print(line)

            if line.strip() == remove_closing_token:
                skip_line = False


# [End Remove]
def run():
    """Run post gen hook functions."""
    remove_donotrender_ext()
    # [Remove]
    copy_hook()
    # [End Remove]
    get_license()


# NOTE: Do not delete this or the hook will not run.
run()
