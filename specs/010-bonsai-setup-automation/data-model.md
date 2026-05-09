# Data Model: Bonsai & Setup

## Entities

### IfcEntity
An architectural object in the Bonsai scene.
- `type`: String (e.g., "IfcWall", "IfcSlab")
- `global_id`: String
- `location`: Tuple[Float, Float, Float]
- `attributes`: Dict[String, Any]

### PrerequisiteStatus
The health of the SDD environment.
- `tool_name`: String (e.g., "spec-kit")
- `is_installed`: Boolean
- `version`: Optional[String]
- `install_command`: Optional[String]

## Relationships
- `BonsaiDriver` (via Blender) creates multiple `IfcEntity` instances.
- `spec-craft` generates an `EnvironmentReport` containing multiple `PrerequisiteStatus` objects.
