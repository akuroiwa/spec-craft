# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = source
BUILDDIR      = _build

# Internal variables.
ALLSPHINXOPTS   = -d $(BUILDDIR)/doctrees $(SPHINXOPTS) $(SOURCEDIR)

.PHONY: help html gettext ja clean

help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo "  html       to make standalone HTML files in English"
	@echo "  gettext    to extract translatable strings into POT files"
	@echo "  ja         to update Japanese translations and build the JA manual"
	@echo "  clean      to remove the build directory"

clean:
	rm -rf $(BUILDDIR)/*

html:
	$(SPHINXBUILD) -M html "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

gettext:
	$(SPHINXBUILD) -b gettext "$(SOURCEDIR)" "$(BUILDDIR)/gettext"

ja:
	sphinx-intl update -p $(BUILDDIR)/gettext -l ja
	$(SPHINXBUILD) -b html "$(SOURCEDIR)" "$(BUILDDIR)/html/ja" -D language='ja' $(SPHINXOPTS)
