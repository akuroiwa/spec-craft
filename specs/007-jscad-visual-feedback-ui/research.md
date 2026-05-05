# Research: JSCAD Visual Feedback & Preview UI

## Decisions

### 1. JSCAD CLI Projections
- **Decision**: Use `npx @jscad/cli <input> --output <output>.svg` for visual feedback.
- **Rationale**: JSCAD natively supports SVG export which provides a vector-based projection suitable for LLM vision analysis.
- **Alternatives**: Rendering to PNG via headless browser (rejected as it adds significant dependency weight).

### 2. Preview Server Implementation
- **Decision**: Use Python's built-in `http.server` combined with a custom `SimpleHTTPRequestHandler` to serve both package resources and the project's `build/` directory.
- **Rationale**: Zero external dependencies (like Flask or FastAPI) keeps the tool lightweight and fast to start.
- **Alternatives**: FastAPI (rejected as overkill for a simple static file server).

### 3. Static Resource Management
- **Decision**: Use `importlib.resources` (available in Python 3.10+) to locate and serve the bundled `index.html` and `STLLoader.js`.
- **Rationale**: Modern, standard-compliant way to access non-code assets within a distributed package.
- **Alternatives**: `pkg_resources` (deprecated).

### 4. Interactive 3D Viewer
- **Decision**: Bundle a minimal `index.html` using Three.js and `STLLoader`. The viewer will accept a filename as a query parameter (e.g., `?model=part.stl`).
- **Rationale**: Provides a consistent, browser-based experience that works across different AI agent environments.

## Best Practices
- **Security**: The web server must only serve files from the `build/` directory and specific package resource folders.
- **Performance**: Use `npx` with a cached version of `@jscad/cli` to avoid repeated downloads.
- **UX**: The `browse` command should automatically open the default system browser using the `webbrowser` module.
