"""Smoke test: proves the package installs, imports and the test runner works."""

import daedalus


def test_package_imports() -> None:
    assert daedalus.__version__ == "0.0.1"
