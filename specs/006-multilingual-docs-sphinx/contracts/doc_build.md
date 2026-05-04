# Build Contract: Documentation Pipeline

## Makefile Targets

### `make html`
- **Purpose**: Build the English documentation.
- **Input**: `docs/source/*.md`
- **Output**: `docs/_build/html/en/`

### `make gettext`
- **Purpose**: Extract translatable strings from sources.
- **Output**: `docs/_build/gettext/*.pot`

### `make ja` (or `sphinx-intl update`)
- **Purpose**: Update Japanese PO files and build the JA manual.
- **Input**: `POT` files + existing `ja.po`
- **Output**: `docs/_build/html/ja/`
