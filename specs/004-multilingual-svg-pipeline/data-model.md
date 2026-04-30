# Data Model: Generation Pipeline

## Entities

### BuildAsset
Represents a generated file in the build directory.
- `output_path`: Path (Absolute path to the asset)
- `domain`: String (e.g., "manga", "cad")
- `language`: String (e.g., "ja", "en", or "universal")
- `timestamp`: DateTime

### SVGTemplate
A source SVG file used for text injection.
- `template_path`: Path
- `placeholder_keys`: List of strings (Extracted from the SVG content)

### Dictionary
Translation data extracted from Obsidian.
- `lang_code`: String
- `translations`: Dict[String, String] (Key-value pairs for replacement)

## Relationships
- A `BuildAsset` is generated from an `SVGTemplate` using a `Dictionary`.
- A `BuildAsset` can also be generated from a `CADSpec`.
- The `BuildManager` tracks all `BuildAsset`s.
