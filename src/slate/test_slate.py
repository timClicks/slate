"""
  Tests for slate
  http://pypi.python.org/slate

  Expected to be used with py.test:
  http://codespeak.net/py/dist/test/index.html
"""

import os
import pytest

from .classes import PDF

@pytest.fixture
def doc():
    with open(get_pdf_path('example.pdf'), 'rb') as f:
        return PDF(f)

@pytest.fixture
def passwd():
    with open(get_pdf_path('protected.pdf'), 'rb') as f:
        return PDF(f, 'a')

def test_basic(doc):
    assert doc[0] == 'This is a test.\n\n\x0c'

def test_metadata_extraction(doc):
    assert doc.metadata

def test_text_method(doc):
    assert "This is a test" in doc.text()

def test_text_method_unclean(doc):
    assert '\x0c' in doc.text(clean=0)

def test_password(passwd):
    assert passwd[0] == "Chamber of secrets.\n\n\x0c"

def get_pdf_path(pdf_file):
    return os.path.join(
        os.path.dirname(__file__),
        pdf_file)


