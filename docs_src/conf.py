# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'My AI website'
copyright = '2025, David TBO'
author = 'David TBO'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'myst_parser',
    'nbsphinx',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary'
]

autosummary_generate = True

# Do not execute Jupyter notebooks during HTML build
nbsphinx_allow_errors = True
nbsphinx_execute = 'never'

# File suffixes and source file types
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

templates_path = ['_templates']
exclude_patterns = [
    '_build',
    'Thumbs.db',
    '.DS_Store',
    'AI/AI_agents/**',
    'AI/Big_Data/**',
    'AI/computer_vision/**',
    'AI/deep_learning/**',
    'AI/LLM/**',
    'AI/machine_learning/optimization/**',
    'AI/machine_learning/supervised_learning/**',
    'AI/machine_learning 2/supervised_learning/**',
    'AI/NLP/**',
    'AI/reinforcement_learning/**',
    '**/.ipynb_checkpoints/**',
]




# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

import sphinx_rtd_theme

html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
