# Quickstart: Documentation Workflow

## Setting up the Doc Environment
```bash
uv add --dev sphinx sphinx-intl myst-parser sphinx_rtd_theme
```

## Building English Manual
```bash
cd docs
make html
```

## Updating Translations (Japanese)
1. Extract strings: `make gettext`
2. Update PO file: `sphinx-intl update -p _build/gettext -l ja`
3. Translate the strings in `docs/source/locale/ja/LC_MESSAGES/*.po`
4. Build Japanese version: `make -e SPHINXOPTS="-D language='ja'" html`
