# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = source
BUILDDIR      = build

SCREENOPTS = -D latex_elements.pointsize=12pt -D latex_elements.classoptions=,openany,oneside -D latex_elements.preamble=\\usepackage{mfgan} -D code_example_wrap=67

serve:
	sphinx-autobuild --host 192.168.1.2 source build/html
pdf:
	$(SPHINXBUILD) -b latex $(SCREENOPTS) $(ALLSPHINXOPTS) $(SOURCEDIR) $(BUILDDIR)/latex
	$(MAKE) -C $(BUILDDIR)/latex all-pdf

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help serve Makefile



# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
