import pytest
import os
import shutil
import tempfile
from pathlib import Path

@pytest.fixture
def temp_workspace():
    """Creates a temporary workspace with standard spec-craft structure."""
    temp_dir = tempfile.mkdtemp()
    workspace_path = Path(temp_dir)
    
    # Setup folders
    (workspace_path / "obsidian").mkdir()
    (workspace_path / ".specify").mkdir()
    
    yield workspace_path
    
    shutil.rmtree(temp_dir)

@pytest.fixture
def mock_git_repo(temp_workspace):
    """Initializes a git repo in the temp workspace."""
    import git
    repo = git.Repo.init(temp_workspace)
    return repo
