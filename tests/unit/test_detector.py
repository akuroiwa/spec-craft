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
    assert "agent_command_path" not in metadata
    assert "agent_command_paths" not in metadata

def test_detector_agent_paths(temp_workspace):
    """Verify detection of multiple agent command paths."""
    (temp_workspace / ".gemini").mkdir()
    (temp_workspace / ".gemini" / "commands").mkdir()
    (temp_workspace / ".agents").mkdir()
    (temp_workspace / ".agents" / "skills").mkdir()
    
    detector = WorkspaceDetector(temp_workspace)
    metadata = detector.get_metadata()
    
    assert "agent_command_paths" in metadata
    assert metadata["agent_command_paths"]["gemini"] == str(temp_workspace / ".gemini" / "commands")
    assert metadata["agent_command_paths"]["agy"] == str(temp_workspace / ".agents" / "skills")
    # agy should be preferred over gemini
    assert metadata["agent_command_path"] == str(temp_workspace / ".agents" / "skills")
