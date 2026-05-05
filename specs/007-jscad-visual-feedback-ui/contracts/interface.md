# Contracts: JSCAD Visuals & UI

## CLI Contract

### `spec-craft browse`
- **Purpose**: Starts the local 3D preview server.
- **Options**:
    - `--port`: Port number (default: 8080)
    - `--no-browser`: Don't open the system browser automatically.
- **Behavior**: Serves `index.html` and the `build/` directory.

## MCP Tool Contract

### `trigger_cad_build`
- **Purpose**: Generates CAD files in multiple formats.
- **Input**:
    - `jscad_code`: String (Source logic)
    - `output_name`: String (Target filename without extension)
    - `formats`: List[String] (e.g., `['stl', 'svg']`)
- **Output**: JSON object with paths to all generated formats.

## Web UI Contract

### `/` (Root)
- **Serves**: `index.html` (The Three.js viewer).
- **Params**: `?model=<path-to-stl>` relative to `build/`.

### `/build/`
- **Serves**: Raw files from the project's build directory.
