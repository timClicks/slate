"""
  Tests for slate 
  http://pypi.python.org/slate

  Expected to be used with py.test:
  http://codespeak.net/py/dist/test/index.html
"""

from slate import PDF

def test_basic_works():
    with open('basic.pdf', 'rb') as f:
        doc = PDF(f)
    assert doc[0] == 'This is a test'

