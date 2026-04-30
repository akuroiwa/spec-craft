# MCP Contract: Generation Pipeline

## Tools

### `trigger_svg_build`
- **Purpose**: Generates a translated SVG from a template and Obsidian dictionary.
- **Input**:
    - `template_path`: String (Relative to `templates/`)
    - `obsidian_path`: String (Path to file containing translations)
    - `lang`: String (e.g., "ja")
- **Output**: Path to the generated asset.

### `trigger_cad_build`
- **Purpose**: Generates an STL file from JSCAD code based on Obsidian requirements.
- **Input**:
    - `jscad_code`: String (The JSCAD source code)
    - `output_name`: String (Filename for the .stl)
- **Output**: Path to the generated STL.

## Prompts

### `build-organization-guide`
- **Role**: Explains the hierarchical structure of the `build/` directory and how to manage language versions.
