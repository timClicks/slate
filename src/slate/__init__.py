#! /usr/env/bin python

"""
slate provides a convenient interface to PDFMiner[1].

Intializing a slate.PDF object will provide you with
the text from the source file as a list of pages. So,
a five page PDF file will have a range of 0-4.

    >>> with open('example.pdf', 'rb') as f:
    ...    PDF(f) #doctest: +ELLIPSIS
    ...
    [..., ..., ..., ...]

Beware of page numbers. slate.PDF objects start at 0.

    >>> with open('example.pdf', 'rb') as f:
    ...    doc = PDF(f)
    ...
    >>> "Hello, I'm page three." in doc[2]
    True

Blank pages are empty strings:

    >>> doc[1]
    ''

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

    >>> with open('protected.pdf', 'rb') as f:
    ...    PDF(f, 'a')[0].strip()
    'Chamber of secrets.'


  [1] http://www.unixuser.org/~euske/python/pdfminer/index.html
  [2] http://www.unixuser.org/~euske/python/pdfminer/programming.html
"""

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

from .classes import PDF
