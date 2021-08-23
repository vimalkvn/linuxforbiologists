# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------
project = 'Linux for Biologists'
copyright = '2021, Vimalkumar Velayudhan'
author = 'Vimalkumar Velayudhan'

# The full version, including alpha/beta/rc tags
release = '2021'
version = '1'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = []

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['build', 'draft.rst']

pygments_style = 'colorful'

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#

html_theme = 'alabaster'
html_theme_options = {
    'font_family':
        '"Source Serif 4", Ubuntu, serif',
    'head_font_family':
        'Fira Sans, Ubuntu, sans-serif',
    'code_font_family': 'monospace, sans-serif',
    'pre_bg': '#efefef',
    'note_bg': '#e6f7ff',
    'note_border': '#ccefff',
    'sidebar_list': '#777777',
    'body_text': '#313131',
    'logo': 'linuxforbiologists-logo.png',
    'logo_name': True,
    'logo_text_align': 'left',
    'show_relbars': True
}
# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# html_title = 'Linux and Programming Cookbook for Biologists'
html_short_title = 'Linux for Biologists'

numfig = True
numfig_secnum_depth = 0

