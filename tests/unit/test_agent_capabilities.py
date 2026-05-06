import pytest
from spec_craft.core.agent import AgentManager, GenerativeDomain

def test_check_generative_capabilities_manga(temp_workspace):
    """Verify that manga capability is correctly reported."""
    manager = AgentManager(temp_workspace)
    capability = manager.check_generative_capabilities(GenerativeDomain.MANGA)
    
    assert capability.domain == GenerativeDomain.MANGA
    assert capability.required_extension == "nano-banana"
    # By default in empty workspace, it should be False
    assert capability.is_ready is False
    assert "extension install nano-banana" in capability.install_command

def test_check_generative_capabilities_cad(temp_workspace):
    """Verify that CAD capability (built-in) is correctly reported."""
    manager = AgentManager(temp_workspace)
    capability = manager.check_generative_capabilities(GenerativeDomain.CAD)
    
    assert capability.domain == GenerativeDomain.CAD
    # CAD is considered built-in via npx
    assert capability.is_ready is True

def test_check_generative_capabilities_installed(temp_workspace):
    """Verify that installed extension makes capability ready."""
    specify_dir = temp_workspace / ".specify"
    specify_dir.mkdir(exist_ok=True)
    (specify_dir / "extensions.yml").write_text("installed: [{extension: 'nano-banana'}]")
    
    manager = AgentManager(temp_workspace)
    capability = manager.check_generative_capabilities(GenerativeDomain.MANGA)
    
    assert capability.is_ready is True
