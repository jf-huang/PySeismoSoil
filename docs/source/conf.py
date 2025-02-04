# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys

sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0, os.path.abspath('../'))


# -- Project information -----------------------------------------------------

project = 'PySeismoSoil'
copyright = '2019, California Institute of Technology'
author = 'Jian Shi'

# The full version, including alpha/beta/rc tags
release = 'v0.5.3'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
    'sphinx.ext.napoleon',
    'sphinx_automodapi.automodapi',
    'sphinx_automodapi.smart_resolver',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'furo'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# NOT sort output in alphabetical order
# https://stackoverflow.com/a/37210251
autodoc_member_order = 'bysource'

# Specify root document: index.rst
root_doc = 'index'


numpydoc_show_class_members = False
automodsumm_inherited_members = True


# ------- A fix to sphinx-automodapi to exclude imported members ---------------
# Thanks to https://github.com/astropy/sphinx-automodapi/issues/119
from sphinx_automodapi import automodsumm  # noqa: E402
from sphinx_automodapi.utils import find_mod_objs  # noqa: E402


def find_mod_objs_patched(*args, **kwargs):
    return find_mod_objs(args[0], onlylocals=True)


def patch_automodapi(app):
    """Monkey-patch the automodapi extension to exclude imported members"""
    automodsumm.find_mod_objs = find_mod_objs_patched


def setup(app):
    app.connect('builder-inited', patch_automodapi)
