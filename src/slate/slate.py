#! /usr/env/bin python

#This file is part of slate.

#slate is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.

#slate is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with slate.  If not, see <http://www.gnu.org/licenses/>.

from StringIO import StringIO

from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter as PI
from pdfminer.pdfdevice import PDFDevice
from pdfminer.converter import TextConverter

__all__ = ['PDF']

class PDFPageInterpreter(PI):
    def process_page(self, page):
        if 1 <= self.debug:
            print >>stderr, 'Processing page: %r' % page
        (x0,y0,x1,y1) = page.mediabox
        if page.rotate == 90:
            ctm = (0,-1,1,0, -y0,x1)
        elif page.rotate == 180:
            ctm = (-1,0,0,-1, x1,y1)
        elif page.rotate == 270:
            ctm = (0,1,-1,0, y1,-x0)
        else:
            ctm = (1,0,0,1, -x0,-y0)
        self.device.outfp.seek(0)
        self.device.outfp.buf = ''
        self.device.begin_page(page, ctm)
        self.render_contents(page.resources, page.contents, ctm=ctm)
        self.device.end_page(page)
        return self.device.outfp.getvalue()

class PDF(list):
    """
    Converts a PDF file into a list of strings. Each page's text
    is converted into an item in the PDF object.

    slate.PDF respects the security settings of the PDF file.

    Arguments:
       :password:   The password for the PDF, if required.

       :just_text:  If False, the __init__ function will preserve
                    font information and images inside the PDF.doc
                    attribute. Refer to PDFMiner's documentation to
                    acess it.

    Attributes:
      :metadata:    The PDF's metadata as a dict, typically includes
                    the creation date, author, title, etc.
    """
    def __init__(self, f, password='', just_text=1):
        self.parser = PDFParser(f)
        self.doc = PDFDocument()
        self.parser.set_document(self.doc)
        self.doc.set_parser(self.parser)
        self.doc.initialize(password)
        if self.doc.is_extractable:
            self.resmgr = PDFResourceManager()
            self.device = TextConverter(self.resmgr, outfp=StringIO())
            self.interpreter = PDFPageInterpreter(
               self.resmgr, self.device)
            for page in self.doc.get_pages():
                self.append(self.interpreter.process_page(page))
        self.metadata = self.doc.info
        if just_text:
            self._cleanup()

    def _cleanup(self):
        """
        Frees lots of non-textual information, such as the fonts
        and images and the objects that were needed to parse the
        PDF.
        """
        del self.device
        del self.doc
        del self.parser
        del self.resmgr
        del self.interpreter
