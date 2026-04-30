# Data Model: Extension & 3D Assets

## Entities

### ExtensionManifest
Definition of the spec-kit extension.
- `extension_id`: String (e.g., "spec-craft")
- `commands`: List of Command objects
- `hooks`: List of Hook objects

### BlenderScript
A generated scene construction script.
- `filename`: String
- `content`: String (Python code)
- `target_version`: String (e.g., "4.0")

### BonkeiScene
A structured 3D scene description.
- `elements`: List of 3D objects (mountain, tree, river)
- `dimensions`: Tray size (x, y, z)
- `lighting`: Time of day/ambience

## Relationships
- An `ExtensionManifest` maps spec-kit commands to `spec-craft` MCP tools.
- A `BlenderScript` is generated from a `BonkeiScene` spec.
- The `BuildManager` organizes `BlenderScript` outputs into `build/3d/`.
