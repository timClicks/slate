""" 
  Tests for slate 
  http://pypi.python.org/slate

  Expected to be used with py.test:
  http://codespeak.net/py/dist/test/index.html
"""

from slate import PDF

def pytest_funcarg__doc(request):
    with open('basic.pdf', 'rb') as f:
        return PDF(f)

def pytest_funcarg__passwd(request):
    with open('passwd-a.pdf') as f:
        return PDF(f, 'a')

def test_basic(doc):
    assert doc[0] == 'This is a test.\x0c'

def test_metadata_extraction(doc):
    assert doc.metadata

def test_text_method(doc):
    assert doc.text() == "This is a test."

def test_text_method_unclean(doc):
    assert '\x0c' in doc.text(clean=0)

def test_password(passwd):
    assert passwd[0] == "Chamber of secrets.\x0c"
