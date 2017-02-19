import unittest

import os
from . import PDF

class TestSlate(unittest.TestCase):
    def setUp(self):
        with open(get_pdf_path('example.pdf'), 'rb') as f:
            self.doc = PDF(f)
        with open(get_pdf_path('protected.pdf'), 'rb') as f:
            self.passwd = PDF(f, 'a')

    def test_basic(self):
        assert self.doc[0] == 'This is a test.\n\n\x0c'

    def test_no_text_carry_over(self):
        assert self.doc[1] == '\x0c'

    def test_metadata_extraction(self):
        assert self.doc.metadata

    def test_text_method(self):
        assert "This is a test" in self.doc.text()

    def test_text_method_unclean(self):
        assert '\x0c' in self.doc.text(clean=0)

    def test_password(self):
        assert self.passwd[0] == "Chamber of secrets.\n\n\x0c"


def get_pdf_path(pdf_file):
    return os.path.join(
        os.path.dirname(__file__),
        pdf_file)

if __name__ == '__main__':
    unittest.main()
