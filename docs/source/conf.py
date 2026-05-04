# Configuration file for the Sphinx documentation builder.

# -- Project information -----------------------------------------------------
project = 'Spec-Craft'
copyright = '2026, Akihiro'
author = 'Akihiro'
release = '0.1.0'

# -- General configuration ---------------------------------------------------
extensions = [
    'myst_parser',
    'sphinx_rtd_theme',
]

templates_path = ['_templates']
exclude_patterns = []

# Localization
language = 'en'
locale_dirs = ['locale/']
gettext_compact = False

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# MyST settings
myst_enable_extensions = [
    "colon_fence",
    "deflist",
]
