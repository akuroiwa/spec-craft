import pytest
from pathlib import Path
from unittest.mock import patch, MagicMock
from spec_craft.core.emacs import EmacsManager

def test_emacs_manager_init(temp_workspace):
    manager = EmacsManager(temp_workspace)
    assert manager.project_root == temp_workspace
    assert ".spec-craft" in str(manager.sandbox_dir)
    assert "spec_craft_" in manager.socket_name

def test_emacs_manager_ensure_sandbox(temp_workspace):
    manager = EmacsManager(temp_workspace)
    manager.ensure_sandbox()
    assert (manager.sandbox_dir / "init.el").is_file()

@patch("subprocess.run")
def test_emacs_manager_start_daemon(mock_run, temp_workspace):
    manager = EmacsManager(temp_workspace)
    mock_run.return_value = MagicMock(returncode=0)
    
    # Mock is_daemon_running to return False first, then True
    with patch.object(EmacsManager, "is_daemon_running", side_effect=[False, True]):
        success = manager.start_daemon()
        assert success is True
        assert mock_run.called
        args, kwargs = mock_run.call_args
        command = args[0]
        assert "emacs" in command
        # Verify --daemon argument exists
        assert any("--daemon=" in arg for arg in command)

@patch("subprocess.run")
def test_emacs_manager_execute_command(mock_run, temp_workspace):
    manager = EmacsManager(temp_workspace)
    mock_run.return_value = MagicMock(returncode=0, stdout="Result")
    
    with patch.object(EmacsManager, "is_daemon_running", return_value=True):
        result = manager.execute_command("(+ 1 1)")
        assert result == "Result"
        assert mock_run.called
        args, kwargs = mock_run.call_args
        command = args[0]
        assert "emacsclient" in command
        assert "(+ 1 1)" in command
