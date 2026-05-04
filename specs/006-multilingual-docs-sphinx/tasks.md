# Tasks: Multilingual Documentation with Sphinx and gettext

## Implementation Strategy
We will implement the multilingual documentation system by first setting up the Sphinx environment with MyST-Parser and the necessary dev dependencies via `uv`. Then, we will write the core manual pages in English Markdown. Finally, we will establish the `gettext` workflow to extract strings and create the Japanese translation files (`.po`), followed by build automation using a Makefile.

## Phase 1: Setup
- [X] T001 Add Sphinx dev dependencies (`sphinx`, `sphinx-intl`, `myst-parser`, `sphinx_rtd_theme`) using `uv add --dev`
- [X] T002 Initialize Sphinx project structure in `docs/` using `sphinx-quickstart`
- [X] T003 Configure `docs/source/conf.py` to support MyST-Parser, RTD theme, and localization (gettext_compact=False)

## Phase 2: Foundational
- [X] T004 Create `docs/Makefile` with targets for `html`, `gettext`, and automated JA build
- [X] T005 [P] Create base English Markdown files: `docs/source/index.md`, `docs/source/strategy.md`, `docs/source/installation.md`, `docs/source/domain-guides.md`

## Phase 3: User Story 2 - Strategy vs Tactics Documentation (Priority: P2)
**Goal**: Clearly explain the "Strategy (Obsidian) vs Tactics (spec-kit)" analogy in the manual.
**Independent Test**: Build HTML and verify the "Concept" or "Strategy" section content.

- [X] T006 [US2] Write detailed "Strategy vs Tactics" content in `docs/source/strategy.md`
- [X] T007 [US2] Document installation and AI agent setup in `docs/source/installation.md`
- [X] T008 [US2] Document domain-specific guides (Manga, CAD, 3D) in `docs/source/domain-guides.md`

## Phase 4: User Story 1 - Multi-language Manual Access (Priority: P1)
**Goal**: Establish the Japanese translation pipeline and build both EN and JA versions.
**Independent Test**: Verify English output in `docs/_build/html/en/` and Japanese output in `docs/_build/html/ja/`.

- [X] T009 [US1] Extract translatable strings to POT files using `make gettext` in `docs/`
- [X] T010 [US1] Initialize Japanese translation catalog using `sphinx-intl update -p _build/gettext -l ja` in `docs/`
- [X] T011 [P] [US1] Provide initial Japanese translations in `docs/source/locale/ja/LC_MESSAGES/*.po`
- [X] T012 [US1] Build both EN and JA HTML versions and verify directory organization

## Phase 5: Polish
- [X] T013 Run `sphinx-build -b linkcheck` to ensure no broken external links in the manual
- [X] T014 Final verification of all success criteria (SC-001 to SC-004) in Phase 6 spec

## Dependencies
- US2 (Content) depends on Phase 1 & 2 (Setup & Foundational).
- US1 (Localization) depends on US2 (Content) being complete to extract strings.

## Parallel Execution Examples
- T005 and T004 can be started once T002 is done.
- T011 can be worked on as soon as T010 extracts the initial strings.
