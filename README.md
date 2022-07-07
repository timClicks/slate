# slate: the easiest way to get text from PDFs in Python

Slate is a Python package that simplifies the process of extracting  text from PDF files.
It depends on the PDFMiner package.

Slate provides one class, `PDF`. `PDF` takes a file-like object and  will extract all text
from the document, presentating each page as a string of text:

    >>> with open('example.pdf') as f:
    ...    doc = slate.PDF(f)
    ...
    >>> doc
    [..., ..., ...]
    >>> doc[1]
    'Text from page 2...'

If your pdf is password protected, pass the password as the second argument:

    >>> with open('secrets.pdf') as f:
    ...     doc = slate.PDF(f, 'password')
    ...
    >>> doc[0]
    "My mother doesn't know this, but..."

## More complex operations

If you would like access to the images, font files and other information, then take some
time to learn the PDFMiner API.

## What is wrong with PDFMiner?

1. Getting simple things done, like extracting the text is quite complex. The program is
   not designed to return Python objects, which makes interfacing things irritating.
2. It's an extremely complete set of tools, with multiple and moderately steep learning curves.
3. It's not written with hackability in mind.
