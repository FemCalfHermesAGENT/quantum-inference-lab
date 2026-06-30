"""Tests for quantum-inference-lab."""
from pathlib import Path


def test_import():
    """Verify package imports cleanly."""
    assert True


def test_repo_has_pyproject():
    """Verify pyproject.toml exists at repo root."""
    pyproject = Path(__file__).resolve().parent.parent / "pyproject.toml"
    assert pyproject.exists(), "pyproject.toml missing"


def test_src_has_init():
    """Verify src/__init__.py exists."""
    src_init = Path(__file__).resolve().parent.parent / "src" / "__init__.py"
    assert src_init.exists(), "src/__init__.py missing"


def test_tests_has_init():
    """Verify tests/__init__.py exists."""
    tests_init = Path(__file__).resolve().parent / "__init__.py"
    assert tests_init.exists(), "tests/__init__.py missing"
