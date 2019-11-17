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
import os
import re
import sys

sys.path.insert(0, os.path.abspath("."))


# -- Project information -----------------------------------------------------

project = "Python Keybase Bot"
copyright = "2019, keybase"
author = "keybase"

# The full version, including alpha/beta/rc tags
# [CUSTOM] We will be getting this from the peotry file
# Done this way to as to avoid reliance on a toml parser

try:
    with open("../pyproject.toml") as handle:
        lines = handle.read().splitlines()
        version = (
            list(
                map(
                    lambda s: re.fullmatch('^version = ".+"$', s),
                    filter(lambda s: "version = " in s, lines),
                )
            )[0]
            .string.split()[-1]
            .replace('"', "")
        )
        release = version
except Exception as e:
    print("Unable to detect version from poetry. This is done in docsrc/conf.py")
    raise e


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx_rtd_theme",
    "sphinx_autodoc_typehints",
    "sphinx.ext.napoleon",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]
