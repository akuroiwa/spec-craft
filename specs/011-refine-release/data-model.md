# Data Model: Refinement & Staging

## Entities

### RefinedCADResult
Result containing multi-format paths.
- `stl_path`: Path
- `svg_path`: Path
- `source_js`: Path

### IFCProject
A project initialized via Bonsai.
- `ifc_file`: String (IFC 2x3 or IFC 4)
- `units`: String (Millimeters/Meters)

### ReleaseStaging
Status of the Test PyPI upload.
- `version`: String
- `target`: String ("testpypi")
- `is_verified`: Boolean

## Relationships
- `CADDriver` is refined to produce `RefinedCADResult`.
- `ReleaseStaging` is the last gate before `main` PyPI.
