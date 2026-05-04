# Data Model: Documentation Assets

## Entities

### ManualSource
The English Markdown source files.
- `filename`: String (e.g., `index.md`, `installation.md`)
- `content`: Markdown text

### TranslationCatalog (POT)
The template for all translatable strings.
- `strings`: List of unique text blocks extracted from `ManualSource`

### LocalizedCatalog (PO)
The language-specific translation file.
- `language_code`: String (`ja`)
- `mappings`: Dict[String, String] (English -> Japanese)

## Relationships
- `POT` is generated from `ManualSource`.
- `PO` is updated from `POT`.
- `Sphinx Build` uses `ManualSource` and `PO` to generate HTML.
