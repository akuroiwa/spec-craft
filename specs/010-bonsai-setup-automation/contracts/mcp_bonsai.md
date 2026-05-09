# MCP Contract: Bonsai & Setup Automation

## Tools

### `check_environment`
- **Purpose**: Detect missing prerequisites for the full Spec-Craft pipeline.
- **Input**: None
- **Output**: JSON list of `PrerequisiteStatus` objects.

## Prompts

### `bonsai-architectural-guide`
- **Role**: Provides guidance for IFC-compliant modeling within the SDD workflow.
- **Rules**: Use standard IFC classes, manage spatial containers (Site, Building, Story).

### `test-pypi-release-checklist`
- **Role**: A step-by-step guide for performing the first release to Test PyPI.
