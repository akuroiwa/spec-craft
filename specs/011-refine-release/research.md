# Research: Final Refinement & Release Preparation

## Decisions

### 1. Dual Format JSCAD Output
- **Decision**: Execute `npx @jscad/cli` twice or use a serial execution logic in `CADDriver`.
- **Rationale**: JSCAD CLI typically takes one output path. To ensure both STL (for production) and SVG (for vision) are generated, a reliable sequential build is necessary.
- **Alternatives**: Using a custom wrapper (rejected as it adds another moving part).

### 2. Bonsai IFC Logic
- **Decision**: Update the script generator to use the `bonsai` module (successor to `blenderbim`) and `bpy.ops.bim.create_project()` for initialization.
- **Rationale**: Verified from research in the Bonsai repository. Ensures compliance with the latest OpenBIM standards.
- **Alternatives**: Legacy `blenderbim` naming (rejected as it's being phased out).

### 3. Comprehensive Setup Detection
- **Decision**: Extend `check_environment` to search for `node_modules` for `@jscad/modeling` and `@jscad/cli`, and use `bpy.utils.addons_fake_it` or checking `bpy.context.preferences.addons` for the Bonsai add-on.
- **Rationale**: Provides much deeper environmental awareness than just checking for binary availability.

### 4. Test PyPI Upload
- **Decision**: Use `twine` for the staging release to Test PyPI.
- **Rationale**: Twine is the standard tool for secure PyPI uploads and supports the `testpypi` repository explicitly.

## Best Practices
- **Localization**: Use the same technical terms (e.g., "Strategy", "Tactics") in Japanese to avoid confusion.
- **Validation**: Perform the "Gold Master" integration test *after* the local package build to ensure data files are correctly loaded from the wheel environment.
