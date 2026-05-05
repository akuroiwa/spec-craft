import pytest
from pathlib import Path
from spec_craft.core.ui.server import PreviewRequestHandler

def test_handler_translate_path(temp_workspace):
    """Verify that the handler correctly maps virtual paths to real files."""
    # Mock class to test only translate_path logic
    class MockHandler(PreviewRequestHandler):
        def __init__(self, project_root):
            self.project_root = project_root
            # Skip base init
        def log_message(self, format, *args): pass

    handler = MockHandler(temp_workspace)
    
    # 1. Static resources (should point to src/spec_craft/static in dev/test)
    index_path = handler.translate_path("/index.html")
    assert "index.html" in index_path
    assert "spec_craft" in index_path
    
    # 2. Build assets
    # Setup a dummy build file
    build_file = temp_workspace / "build" / "cad" / "universal" / "part.stl"
    build_file.parent.mkdir(parents=True, exist_ok=True)
    build_file.write_text("stl data")
    
    translated_build_path = handler.translate_path("/build/cad/universal/part.stl")
    assert str(build_file) == translated_build_path

def test_handler_traversal_protection(temp_workspace):
    """Verify directory traversal protection."""
    class MockHandler(PreviewRequestHandler):
        def __init__(self, project_root): self.project_root = project_root
        def log_message(self, format, *args): pass

    handler = MockHandler(temp_workspace)
    assert handler.translate_path("/build/../../secret.txt") == ""
