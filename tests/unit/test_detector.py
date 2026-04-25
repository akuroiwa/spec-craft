import pytest
from pathlib import Path
from spec_craft.core.detector import WorkspaceDetector

def test_detector_finds_obsidian_and_specify(temp_workspace):
    """Verify that detector correctly identifies existing directories."""
    detector = WorkspaceDetector(temp_workspace)
    assert detector.root_path == temp_workspace
    assert detector.obsidian_path == temp_workspace / "obsidian"
    assert detector.specify_path == temp_workspace / ".specify"
    assert detector.is_git_repo is False

def test_detector_with_git(temp_workspace, mock_git_repo):
    """Verify git repo detection."""
    detector = WorkspaceDetector(temp_workspace)
    assert detector.is_git_repo is True
    assert detector.root_path == temp_workspace

def test_detector_metadata(temp_workspace):
    """Verify metadata dictionary content."""
    detector = WorkspaceDetector(temp_workspace)
    metadata = detector.get_metadata()
    assert metadata["is_git_repo"] is False
    assert metadata["obsidian_path"].endswith("obsidian")
