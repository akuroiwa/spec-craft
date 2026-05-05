# Data Model: JSCAD Visual Feedback & UI

## Entities

### CADBuildResult
Result of a multi-format CAD generation.
- `stl_path`: Path (Absolute path to the STL file)
- `svg_path`: Path (Absolute path to the SVG projection)
- `success`: Boolean
- `error_message`: Optional[String]

### PreviewServer
State of the local preview environment.
- `port`: Integer (Default: 8080)
- `root_dir`: Path (The project build/ directory)
- `server_url`: String (e.g., "http://localhost:8080")

### VisualProjection
Metadata about the generated SVG.
- `view_angle`: String (e.g., "perspective", "top")
- `dimensions`: Dict[String, Float] (Width, height in mm)

## Relationships
- `CADDriver` produces a `CADBuildResult`.
- `PreviewServer` provides access to `CADBuildResult` artifacts via a web browser.
