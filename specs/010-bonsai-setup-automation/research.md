# Research: Bonsai Integration & Setup Automation

## Decisions

### 1. Bonsai (BlenderBIM) API Integration
- **Decision**: Focus on generating Python scripts that leverage the `ifcopenshell` and `blenderbim` (now Bonsai) modules.
- **Rationale**: This follows the established pattern of generating `.py` scripts for Blender. The Bonsai add-on provides high-level operators for IFC entities.
- **Alternatives**: Direct IFC file generation (rejected as it is less interactive for the user).

### 2. Setup Automation Tool
- **Decision**: Implement `check_environment` as an MCP tool that returns a detailed status report and actionable fix commands.
- **Rationale**: Proactive detection prevents frustrating runtime errors. Providing the exact `pip install` or `npx` commands improves UX.
- **Alternatives**: Automatic background installation (rejected due to security and user control concerns).

### 3. Test PyPI Release Guide
- **Decision**: Include a dedicated section in the `Release Engineering` guide for Test PyPI.
- **Rationale**: Provides a safe "staging" environment for the first release, ensuring that the package metadata and dependencies are correct.

## Best Practices
- **BIM Consistency**: Always include IFC attributes (GlobalId, PredefinedType) in the generated code to ensure architectural integrity.
- **Dependency Detection**: Use `shutil.which` and `importlib.util.find_spec` for robust prerequisite checking.
- **Multi-language QA**: Perform a final pass on all Japanese `.po` files to ensure technical terms (BIM, SDD, etc.) are consistent.
