# Data Model: Vision & Sandbox

## Entities

### BlenderRenderRequest
A request to generate a visual projection of a 3D scene.
- `scene_script`: Path (to the .py script)
- `output_format`: String ("svg")
- `view_type`: Enum (TOP, FRONT, PERSPECTIVE)

### EmacsDaemonSession
An isolated editing environment instance.
- `project_id`: String (unique hash)
- `init_dir`: Path (e.g., .spec-craft/emacs/)
- `socket_name`: String
- `status`: Enum (STARTING, RUNNING, STOPPED)

### LSPDiagnostic
Feedback from the language server.
- `file`: Path
- `line`: Integer
- `message`: String
- `severity`: Enum (ERROR, WARNING, INFO)

## Relationships
- `spec-craft` manages multiple `EmacsDaemonSession` instances.
- A `BlenderRenderRequest` produces one or more SVG artifacts for AI analysis.
