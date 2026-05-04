# Feature Specification: Multilingual Documentation with Sphinx and gettext

**Feature Branch**: `006-multilingual-docs-sphinx`  
**Created**: 2026-04-25  
**Status**: Draft  
**Input**: User description: "Phase 6: Multilingual Documentation with Sphinx and gettext"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Multi-language Manual Access (Priority: P1)

As a spec-craft user, I want to read the tool's manual in both English and Japanese so that I can understand how to use the SDD toolkit regardless of my primary language.

**Why this priority**: Documentation is critical for adoption. Providing it in the user's native language (JA) and the lingua franca of engineering (EN) is essential.

**Independent Test**: Can be tested by running the Sphinx build command and verifying that both English (`_build/html/en/index.html`) and Japanese (`_build/html/ja/index.html`) versions are generated.

**Acceptance Scenarios**:

1. **Given** the documentation source, **When** I run the build command, **Then** an English HTML manual is created.
2. **Given** translated strings in `.po` files, **When** I run the localized build, **Then** a Japanese HTML manual is created with translated content.

---

### User Story 2 - Strategy vs Tactics Documentation (Priority: P2)

As a creator, I want the manual to clearly explain the "Strategy (Obsidian) vs Tactics (spec-kit)" analogy so that I can follow the intended SDD philosophy.

**Why this priority**: This analogy is the "soul" of the project and differentiates spec-craft from simple task managers.

**Independent Test**: Can be tested by inspecting the rendered "Concept" section of the manual for the Strategy/Tactics diagram and explanation.

**Acceptance Scenarios**:

1. **Given** the rendered manual, **When** I navigate to the Concept section, **Then** I see the explanation of how Obsidian provides the roadmap while spec-kit handles tactical implementation.

---

### Edge Cases

- **Missing Translations**: What if a new English section is added but not yet translated to Japanese? (Assumed: Sphinx falls back to English for that specific section).
- **Broken Links**: What if a link between manual pages is broken in one language? (Assumed: Build process reports broken links as warnings/errors).

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST use Sphinx with `myst-parser` to support Markdown-based documentation.
- **FR-002**: System MUST implement the `gettext` workflow using `sphinx-intl` for localization.
- **FR-003**: System MUST provide a build script (or Makefile) that automates the `make gettext`, `sphinx-intl update`, and `sphinx-intl build` steps.
- **FR-004**: Manual MUST include sections for: Concept (Strategy vs Tactics), Installation (uv/pip), Setup (AI Agent settings), and Domain Guides (Manga, CAD, 3D).
- **FR-005**: All English sources MUST be translated into Japanese using `.po` files.

### Key Entities *(include if feature involves data)*

- **POT File**: Template for all translatable strings extracted from source files.
- **PO File**: Language-specific translation file (e.g., `ja.po`).
- **Sphinx Build**: The final HTML output organized by language code.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Documentation build time (all languages) takes less than 20 seconds.
- **SC-002**: 100% of core documentation sections (Concept, Install, Usage) are translated into Japanese.
- **SC-003**: The build process produces zero fatal errors or broken cross-references.
- **SC-004**: The generated manual is accessible via a simple web browser.

## Assumptions

- **Sphinx Knowledge**: Assumes the AI has the capability to write RST/Markdown and manage Sphinx configuration (`conf.py`).
- **Translation Work**: The AI will provide initial translations, but the user (Akihiro) will review and refine the Japanese nuance.
- **Environment**: Assumes `uv` is used to manage Sphinx and its dependencies.
