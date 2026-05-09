# Build Contract: Refined Generation

## Driver Methods

### `CADDriver.build(code, base_path, formats)`
- **Updates**: Must handle sequential calls for `stl` and `svg`.
- **Imports**: Must use `@jscad/modeling` primitives and booleans correctly.

### `BonsaiDriver.generate_ifc_script(spec, output_path)`
- **Updates**: Use `import bonsai` and `bpy.ops.bim.create_project()`.

## Environment Detection

### `check_environment()`
- **New Checks**:
    - `@jscad/modeling` and `@jscad/cli` in `node_modules/` or global.
    - `bonsai` add-on in Blender configuration.
