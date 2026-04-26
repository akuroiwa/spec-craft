import pytest
from pathlib import Path
from spec_craft.core.agent import AgentManager

def test_agent_manager_registered_extensions(temp_workspace):
    """Verify that manager identifies registered extensions from yaml."""
    specify_dir = temp_workspace / ".specify"
    # specify_dir is created by temp_workspace fixture in conftest.py
    ext_file = specify_dir / "extensions.yml"
    ext_file.write_text("""
installed:
  - extension: git
    command: speckit.git.initialize
  - extension: nano-banana
    command: nanobanana.gen
""")
    
    manager = AgentManager(temp_workspace)
    status = manager.get_extension_status(["git", "not-installed"])
    
    assert status[0].name == "git"
    assert status[0].is_installed is True
    assert status[0].install_command is None
    
    assert status[1].name == "not-installed"
    assert status[1].is_installed is False
    assert "gemini-cli extension install not-installed" in status[1].install_command

def test_agent_manager_missing_file(temp_workspace):
    """Verify behavior when extensions.yml is missing."""
    manager = AgentManager(temp_workspace)
    status = manager.get_extension_status(["any"])
    assert status[0].is_installed is False
