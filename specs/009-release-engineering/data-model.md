# Data Model: Release Engineering

## Entities

### Workflow
Automation definition.
- `name`: String
- `trigger_event`: String (e.g., "push", "release")
- `jobs`: List of Job objects

### ReleaseArtifact
The result of a build.
- `type`: Enum (WHEEL, SDIST)
- `filename`: String
- `content_hashes`: List of SHA256

### DistributionConfig
Packaging settings in `pyproject.toml`.
- `backend`: String ("setuptools")
- `include_data`: List of glob patterns

## Relationships
- A `Workflow` produces one or more `ReleaseArtifact`s.
- `DistributionConfig` determines which files are included in the `ReleaseArtifact`.
