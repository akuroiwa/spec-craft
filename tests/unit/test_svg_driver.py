import pytest
from pathlib import Path
from lxml import etree
from spec_craft.core.drivers.svg import SVGDriver

def test_svg_inject_text_by_id(temp_workspace):
    """Verify text injection using element IDs."""
    template_path = temp_workspace / "template.svg"
    template_path.write_text('<svg xmlns="http://www.w3.org/2000/svg"><text id="greeting">Hello</text></svg>')
    
    output_path = temp_workspace / "output.svg"
    driver = SVGDriver()
    driver.inject_text(template_path, output_path, {"greeting": "こんにちは"})
    
    # Verify result
    tree = etree.parse(str(output_path))
    root = tree.getroot()
    text_el = root.find(".//*[@id='greeting']")
    assert text_el.text == "こんにちは"

def test_svg_inject_text_by_placeholder(temp_workspace):
    """Verify text injection using {{key}} placeholders."""
    template_path = temp_workspace / "template.svg"
    template_path.write_text('<svg xmlns="http://www.w3.org/2000/svg"><text>Greetings, {{name}}!</text></svg>')
    
    output_path = temp_workspace / "output.svg"
    driver = SVGDriver()
    driver.inject_text(template_path, output_path, {"name": "Gemini"})
    
    # Verify result
    result_text = output_path.read_text()
    assert "Greetings, Gemini!" in result_text
