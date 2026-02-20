# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'FactorialHR'
copyright = '2026, Leon Budnick'
author = 'Leon Budnick'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.viewcode',
    'sphinx.ext.coverage',
    'sphinx_rtd_theme',
]

import pathlib
import sys

# Add the src directory to the Python path so Sphinx can find the modules
sys.path.insert(0, pathlib.Path('../src').resolve())

templates_path = ['_templates']
exclude_patterns = []

# -- Options for autosummary -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/extensions/autosummary.html#configuration

autosummary_generate = True  # Automatically generate stub files

# Suppress "more than one target found for cross-reference 'type'" warnings:
# many models (WebhookSubscription, CardPayment, Transaction, etc.) have an
# attribute named "type", so unqualified refs to "type" are ambiguous.
suppress_warnings = ['ref.python']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
