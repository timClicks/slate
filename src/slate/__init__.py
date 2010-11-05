#! /usr/env/bin python

"""
slate provides a convenient interface to PDFMiner[1].

Intializing a slate.PDF object will provide you with
the text from the source file as a list of pages. So,
a five page PDF file will have a range of 0-4.

    >>> with open('example.pdf', 'rb') as f:
    ...    PDF(f)
    ...
    [..., ..., ..., ...]

Beware of page numbers. slate.PDF objects start at 0.

    >>> with open('example.pdf', 'rb') as f:
    ...    doc = PDF(f)
    ...
    >>> doc[2]
    "Hello, I'm page three."

Passwords are supported. Use them as the second argument
of your intialization. Currently, UTF-8 encoding is 
hard-coded. If you would like to access more advanced 
features, you should take a look at the PDFMiner API[2].


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

from slate import PDF
