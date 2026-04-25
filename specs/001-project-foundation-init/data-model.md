# Data Model: Spec-Craft Foundation

## Entities

### Workspace
Represents the project environment.
- `root_path`: Path (Absolute path to project root)
- `obsidian_path`: Path (Path to obsidian/ directory)
- `is_git_repo`: Boolean (Whether root_path is a git repository)
- `specify_path`: Path (Path to .specify/ directory)

### Configuration
Package settings.
- `version`: String (Semantic versioning)
- `dependencies`: List of strings

## Relationships
- A `Workspace` contains a `SpecifyDirectory` and an `ObsidianDirectory`.
- A `Workspace` is managed by a `GitRepository` (optional but encouraged).
