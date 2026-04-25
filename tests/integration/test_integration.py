import pytest
from spec_craft.core.detector import WorkspaceDetector
from spec_craft.core.manager import ConstitutionManager

def test_integration_spec_kit_detection(temp_workspace):
    """Verify that spec-craft can detect spec-kit files in a real-world scenario."""
    # Setup mock spec-kit structure
    specify_dir = temp_workspace / ".specify"
    constitution_path = specify_dir / "memory" / "constitution.md"
    constitution_path.parent.mkdir(parents=True)
    constitution_path.write_text("# Original Constitution")
    
    detector = WorkspaceDetector(temp_workspace)
    manager = ConstitutionManager(detector)
    
    assert detector.specify_path == specify_dir
    assert manager.constitution_path == constitution_path
    
    # Test modification
    manager.append_rule("New Rule", "Details of the new rule.")
    content = constitution_path.read_text()
    assert "### New Rule" in content
    assert "Details of the new rule." in content
