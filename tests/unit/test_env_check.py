import pytest
from pathlib import Path
from spec_craft.core.detector import WorkspaceDetector

def test_check_environment_detects_obsidian(temp_workspace):
    """Verify that obsidian absence is detected."""
    # temp_workspace fixture already creates 'obsidian/'
    detector = WorkspaceDetector(temp_workspace)
    report = detector.check_environment()
    
    obsidian_status = next(s for p in report if (s := p)["tool_name"] == "obsidian")
    assert obsidian_status["is_installed"] is True

def test_check_environment_missing_obsidian(temp_workspace):
    """Verify that missing obsidian is reported."""
    import shutil
    shutil.rmtree(temp_workspace / "obsidian")
    
    detector = WorkspaceDetector(temp_workspace)
    report = detector.check_environment()
    
    obsidian_status = next(s for p in report if (s := p)["tool_name"] == "obsidian")
    assert obsidian_status["is_installed"] is False
    assert "mkdir -p" in obsidian_status["install_command"]
