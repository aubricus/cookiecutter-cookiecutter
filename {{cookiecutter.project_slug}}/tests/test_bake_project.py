from contextlib import contextmanager

import os
import subprocess


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
    extra_context = {}
    baked = cookies.bake(extra_context=extra_context)
    assert baked.exit_code == 0
    assert baked.exception is None


def test_run_black(cookies):
    """Test template files are formatted."""
    result = cookies.bake(extra_context={"project_slug": "black_compat"})
    with inside_dir(str(result.project)):
        call_result = subprocess.check_call(["black"])
