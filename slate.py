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

from pdfminer import converter, layout, pdfinterp, pdfparser

__all__ = ["PDF"]


class PDFPageInterpreter(pdfinterp.PDFPageInterpreter):
    def process_page(self, page):
        x0, y0, x1, y1 = page.mediabox
        if page.rotate == 90:
            ctm = (0, -1, 1, 0, -y0, x1)
        elif page.rotate == 180:
            ctm = (-1, 0, 0, -1, x1, y1)
        elif page.rotate == 270:
            ctm = (0, 1, -1, 0, y1, -x0)
        else:
            ctm = (1, 0, 0, 1, -x0, -y0)
        self.device.outfp.seek(0)
        self.device.outfp.truncate(0)
        self.device.begin_page(page, ctm)
        self.render_contents(page.resources, page.contents, ctm=ctm)
        self.device.end_page(page)
        return self.device.outfp.getvalue()


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
        self.parser = pdfparser.PDFParser(file)
        self.laparams = layout.LAParams(
            char_margin=char_margin, line_margin=line_margin, word_margin=word_margin
        )

        self.doc = pdfparser.PDFDocument()
        self.parser.set_document(self.doc)
        self.doc.set_parser(self.parser)
        self.doc.initialize(password)

        if not check_extractable or self.doc.is_extractable:
            self.resmgr = pdfinterp.PDFResourceManager()
            self.device = converter.TextConverter(
                self.resmgr, outfp=io.StringIO(), laparams=self.laparams
            )
            self.interpreter = PDFPageInterpreter(self.resmgr, self.device)
            for page in self.doc.get_pages():
                self.append(self.interpreter.process_page(page))
            self.metadata = self.doc.info
        if just_text:
            # Free lots of non-textual information, such as the fonts and images and
            # the objects that were needed to parse the PDF
            self.device = None
            self.doc = None
            self.parser = None
            self.resmgr = None
            self.interpreter = None

    def text(self, clean=True):
        """
        Returns the text of the PDF as a single string.
        Options:

          :clean:
            Removes misc cruft, like lots of whitespace.
        """
        s = "".join(self)
        return re.sub(r"\s+", " ", s) if clean else s
