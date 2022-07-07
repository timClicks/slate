r"""
slate provides a convenient interface to PDFMiner[1].

Intializing a slate.PDF object will provide you with
the text from the source file as a list of pages. So,
a five page PDF file will have a range of 0-4.

    >>> with open('tests/example.pdf', 'rb') as f:
    ...    PDF(f) #doctest: +ELLIPSIS
    ...
    [..., ..., ..., ...]

Beware of page numbers. slate.PDF objects start at 0.

    >>> with open('tests/example.pdf', 'rb') as f:
    ...    doc = PDF(f)
    ...
    >>> "Hello, I'm page three." in doc[2]
    True

Blank pages are empty strings:

    >>> doc[1]
    '\x0c'

If you would prefer to access the entire text as a single
string of text, you can call the text method, which will
remove unnecessary whitespace, e.g. '  \n  \x0c' => ' '.

    >>> "Hello" in doc.text()
    True
    >>> '\x0c' in doc.text()
    False

Passwords are supported. Use them as the second argument
of your intialization. Currently, UTF-8 encoding is
hard-coded. If you would like to access more advanced
features, you should take a look at the PDFMiner API[2].

    >>> with open('tests/protected.pdf', 'rb') as f:
    ...    PDF(f, 'a')[0].strip()
    'Chamber of secrets.'


  [1] http://www.unixuser.org/~euske/python/pdfminer/index.html
  [2] http://www.unixuser.org/~euske/python/pdfminer/programming.html
"""

import io
import re
import sys

from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFPageInterpreter, PDFResourceManager
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser

__all__ = ["PDF"]


class PDF(list):
    def __init__(
        self,
        file,
        password="",
        just_text=1,
        check_extractable=True,
        char_margin=1.0,
        line_margin=0.1,
        word_margin=0.1,
    ):
        self.laparams = LAParams(
            char_margin=char_margin, line_margin=line_margin, word_margin=word_margin
        )
        resmgr = PDFResourceManager()
        device = TextConverter(resmgr, outfp=io.StringIO(), laparams=self.laparams)
        interpreter = PDFPageInterpreter(resmgr, device)
        for page in PDFPage.get_pages(
            file, password=password, check_extractable=check_extractable
        ):
            interpreter.process_page(page)
            self.append(device.outfp.getvalue())
            device.outfp = io.StringIO()
        self.metadata = PDFDocument(PDFParser(file), password=password).info
        if just_text:
            self.device = None
            self.resmgr = None
            self.interpreter = None
        else:
            self.device = device
            self.resmgr = resmgr
            self.interpreter = interpreter

    def text(self, clean=True):
        """
        Returns the text of the PDF as a single string.
        Options:

          :clean:
            Removes misc cruft, like lots of whitespace.
        """
        s = "".join(self)
        return re.sub(r"\s+", " ", s) if clean else s
