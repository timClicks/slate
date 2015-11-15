import unittest

from slate import PDF

class TestSlate(unittest.TestCase):
    def setUp(self):
        with open('example.pdf', 'rb') as f:
            self.doc = PDF(f)
        with open('protected.pdf', 'rb') as f:
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

if __name__ == '__main__':
    unittest.main()
