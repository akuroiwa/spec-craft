import subprocess
import pytest

def test_cli_version():
    """Verify 'spec-craft --version' output."""
    result = subprocess.run(
        ["spec-craft", "--version"],
        capture_output=True,
        text=True
    )
    assert result.returncode == 0
    assert "spec-craft" in result.stdout

def test_cli_help():
    """Verify 'spec-craft --help' output."""
    result = subprocess.run(
        ["spec-craft", "--help"],
        capture_output=True,
        text=True
    )
    assert result.returncode == 0
    assert "serve" in result.stdout
