"""
  Tests for slate
  http://pypi.python.org/slate

  Expected to be used with py.test:
  http://codespeak.net/py/dist/test/index.html
"""

import os

import pytest

from slate import PDF

THIS_DIR = os.path.dirname(os.path.abspath(__file__))


@pytest.fixture
def doc():
    with open(os.path.join(THIS_DIR, "example.pdf"), "rb") as f:
        return PDF(f)


@pytest.fixture
def passwd():
    with open(os.path.join(THIS_DIR, "protected.pdf"), "rb") as f:
        return PDF(f, "a")


def test_basic(doc):
    assert doc[0] == "This is a test.\n\n\x0c"


def test_no_text_carry_over(doc):
    assert doc[1] == "\x0c"


def test_metadata_extraction(doc):
    assert doc.metadata


def test_text_method(doc):
    assert "This is a test" in doc.text()


def test_text_method_unclean(doc):
    assert "\x0c" in doc.text(clean=0)


def test_password(passwd):
    assert passwd[0] == "Chamber of secrets.\n\n\x0c"
