import pytest
from spec_craft.core.detector import WorkspaceDetector
from spec_craft.core.manager import ConstitutionManager

def test_manager_finds_constitution(temp_workspace):
    """Verify that manager resolves the constitution path correctly."""
    # Create the file manually in temp workspace
    constitution_path = temp_workspace / ".specify" / "memory" / "constitution.md"
    constitution_path.parent.mkdir(parents=True, exist_ok=True)
    constitution_path.write_text("# Test Constitution")
    
    detector = WorkspaceDetector(temp_workspace)
    manager = ConstitutionManager(detector)
    
    assert manager.constitution_path == constitution_path
    assert manager.read_constitution() == "# Test Constitution"

def test_manager_no_constitution(temp_workspace):
    """Verify behavior when constitution is missing."""
    detector = WorkspaceDetector(temp_workspace)
    manager = ConstitutionManager(detector)
    assert manager.constitution_path is None
    assert manager.read_constitution() is None
