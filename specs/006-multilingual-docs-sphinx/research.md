# Research: Multilingual Documentation with Sphinx & gettext

## Decisions

### 1. Documentation Framework
- **Decision**: Use Sphinx with the `MyST-Parser` extension.
- **Rationale**: MyST allows us to write documentation in Markdown (standard for this project) while leveraging Sphinx's powerful indexing and localization capabilities.
- **Alternatives**: MkDocs (rejected because Sphinx has superior native support for gettext-based localization).

### 2. Localization Workflow
- **Decision**: Implement the standard `gettext` workflow using `sphinx-intl`.
- **Rationale**: This is the industry-standard for translating large documentation projects. It separates content (EN) from translation (PO files), making it easier to manage updates.
- **Alternatives**: Maintaining separate Markdown files for each language (rejected as it is error-prone and hard to keep in sync).

### 3. Build Automation
- **Decision**: Provide a `Makefile` in the `docs/` directory to automate the build process across all languages.
- **Rationale**: Simplifies the developer experience. A single command can handle string extraction, translation updates, and HTML generation.

## Best Practices
- **Content Separation**: Keep source English files in `docs/source/` and translations in `docs/source/locale/`.
- **PO File Management**: Commit `.po` files to the repository to track translation progress.
- **Sphinx Extensions**: Use `sphinx_rtd_theme` for a professional, searchable interface.
