from contextlib import contextmanager

import os
import subprocess
from pathlib import Path


@contextmanager
def inside_dir(dirpath):
    """Execute code from inside the given directory.

    :param dirpath: String, path of the directory the command is being run.
    """
    old_path = os.getcwd()
    try:
        os.chdir(dirpath)
        yield
    finally:
        os.chdir(old_path)


def test_bake(cookies):
    """Test template bake."""
    extra_context = {
        "project_summary": "A summary",
        "project_background": "A background",
        "project_license": "MIT",
        "project_code_of_conduct": "Contributor Covenant",
    }
    baked = cookies.bake(extra_context=extra_context)
    project_path = Path(baked.project)

    assert baked.exit_code == 0
    assert baked.exception is None
    assert project_path.joinpath("LICENSE").is_file()
    assert project_path.joinpath("CODE_OF_CONDUCT.md").is_file()
    assert project_path.joinpath("pyproject.toml").is_file()

    subprocess.run(["black", "--check"], cwd=project_path, check=True)
