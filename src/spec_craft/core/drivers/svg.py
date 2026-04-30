from lxml import etree
from pathlib import Path
from typing import Dict

class SVGDriver:
    """Handles text injection and manipulation in SVG templates."""

    def __init__(self):
        # We handle namespaces to ensure correct element selection
        self.ns = {"svg": "http://www.w3.org/2000/svg"}

    def inject_text(self, template_path: Path, output_path: Path, translations: Dict[str, str]):
        """Injects text from translations into an SVG template."""
        if not template_path.is_file():
            raise FileNotFoundError(f"SVG template not found: {template_path}")

        parser = etree.XMLParser(remove_blank_text=True)
        tree = etree.parse(str(template_path), parser)
        root = tree.getroot()

        # Strategy 1: Replace by ID (id="key")
        for key, value in translations.items():
            element = root.find(f".//*[@id='{key}']", namespaces=self.ns)
            if element is not None:
                element.text = value
                continue

            # Strategy 2: Replace placeholder {{key}} in text nodes
            # This is more intensive as it scans all text
            for el in root.xpath(".//*[text()]"):
                if el.text and f"{{{{{key}}}}}" in el.text:
                    el.text = el.text.replace(f"{{{{{key}}}}}", value)

        # Ensure output directory exists
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Write the modified XML
        tree.write(str(output_path), encoding="utf-8", xml_declaration=True, pretty_print=True)
