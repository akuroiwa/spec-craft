# Research: Multilingual SVG & CAD Pipeline

## Decisions

### 1. SVG Parsing and Text Replacement
- **Decision**: Use `lxml` for SVG XML manipulation.
- **Rationale**: `lxml` is powerful, handles namespaces well, and allows for precise targetting of elements via XPath or ID. It is more robust than the built-in `xml.etree`.
- **Alternatives**: `xml.etree.ElementTree` (rejected due to weaker namespace support and fewer features).

### 2. CAD Integration (JSCAD)
- **Decision**: Wrap `node jscad-tool.js` calls in a `CADDriver` class using `subprocess`.
- **Rationale**: Reuses the established pattern from the user's `gemini-jscad` project. Provides a clear bridge between Python logic and the Node.js toolchain.
- **Alternatives**: Re-implementing JSCAD logic in Python (rejected as it is out of scope and unnecessarily complex).

### 3. Build Directory Organization
- **Decision**: Implement a `BuildManager` that enforces a `<domain>/<lang>/<filename>` structure.
- **Rationale**: Keeps assets organized and prevents naming collisions across different languages and production domains (manga, cad, etc.).
- **Alternatives**: Flat `build/` directory (rejected due to poor scalability).

## Best Practices
- **SVG Placeholders**: Use a consistent pattern for placeholders (e.g., `{{key}}`) or rely on SVG element IDs (e.g., `id="dialogue-1"`) for replacement.
- **JSCAD Modularity**: Encourage the AI to generate modular JSCAD components that can be easily parameterized from the Obsidian spec.
- **Error Handling**: Capture and report specific errors from both the SVG XML parser and the JSCAD Node.js process to guide the user/AI.
