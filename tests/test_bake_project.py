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
    }
    baked = cookies.bake(extra_context=extra_context)
    project_path = Path(baked.project)
    assert baked.exit_code == 0
    assert baked.exception is None
    assert project_path.joinpath("pyproject.toml").is_file()


def test_run_black(cookies):
    """Test template files are formatted."""
    extra_context = {
        "project_summary": "A summary",
        "project_background": "A background",
    }
    result = cookies.bake(extra_context=extra_context)
    with inside_dir(str(result.project)):
        call_result = subprocess.check_call(["black"])
