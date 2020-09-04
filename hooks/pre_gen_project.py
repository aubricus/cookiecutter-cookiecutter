"""Cookiecutter pre_gen_project hook.

See: https://cookiecutter.readthedocs.io/en/1.7.2/advanced/hooks.html
"""

import os
import shutil
import fileinput
from pathlib import Path


# [Remove]
# NOTE: The above directive is used to remove this section during copy_hook
def copy_hook():
    """Copy this repo's pre_gen_project hook to the template."""
    src = Path(__file__)
    dest = Path.cwd().joinpath("hooks/pre_gen_project.py")

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
    """Run pre gen hook functions."""
    # [Remove]
    copy_hook()
    # [End Remove]


# NOTE: Do not delete this or the hook will not run.
run()
