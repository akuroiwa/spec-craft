import pytest
from pathlib import Path
from spec_craft.core.executor import ScriptExecutor

def test_executor_executes_script(temp_workspace):
    """Verify that executor can run a dummy bash script."""
    scripts_dir = temp_workspace / ".specify" / "scripts" / "bash"
    scripts_dir.mkdir(parents=True, exist_ok=True)
    
    dummy_script = scripts_dir / "hello.sh"
    dummy_script.write_text("#!/bin/bash\necho 'Hello from script'\n")
    dummy_script.chmod(0o755)
    
    executor = ScriptExecutor(temp_workspace)
    result = executor.execute("hello.sh")
    
    assert result["exit_code"] == 0
    assert "Hello from script" in result["stdout"]

def test_executor_security_violation(temp_workspace):
    """Verify that executor blocks scripts outside the allowed directory."""
    outside_script = temp_workspace / "evil.sh"
    outside_script.write_text("echo 'evil'")
    
    executor = ScriptExecutor(temp_workspace)
    with pytest.raises(ValueError, match="Security violation"):
        executor.execute("../../../evil.sh")

def test_executor_missing_script(temp_workspace):
    """Verify behavior when script is missing."""
    # Ensure directory exists but script doesn't
    (temp_workspace / ".specify" / "scripts" / "bash").mkdir(parents=True, exist_ok=True)
    
    executor = ScriptExecutor(temp_workspace)
    with pytest.raises(FileNotFoundError):
        executor.execute("ghost.sh")
