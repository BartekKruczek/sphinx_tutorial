# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Gower-metric'
copyright = '2025, gower-metric developers'
author = 'gower-metric developers'

release = '1.4.0'
version = '1.4.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.napoleon',
    'sphinx_copybutton',
]

# enable google and numpy style docstrings
napoleon_google_docstring = True
napoleon_numpy_docstring = True

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = "pydata_sphinx_theme"

# -- Options for EPUB output
epub_show_urls = 'footnote'
