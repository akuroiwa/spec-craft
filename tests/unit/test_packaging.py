import pytest
from importlib import resources
from pathlib import Path

def test_static_resources_accessible():
    """Verify that index.html and viewer.js are accessible via importlib.resources."""
    # Check index.html
    p_html = resources.files("spec_craft.static").joinpath("index.html")
    assert p_html.is_file()
    
    # Check viewer.js
    p_js = resources.files("spec_craft.static").joinpath("viewer.js")
    assert p_js.is_file()

def test_extension_directory_bundling():
    """Verify that the extension directory is accessible via resources."""
    p_ext = resources.files("spec_craft.data").joinpath("extension")
    assert p_ext.is_dir()
    assert p_ext.joinpath("extension.yml").is_file()
