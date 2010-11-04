#!/usr/bin/env python

from distutils.core import setup
from sys import version
if version < '2.2.3':
    from distutils.dist import DistributionMetadata
    DistributionMetadata.classifiers = None
    DistributionMetadata.download_url = None


setup(name='slate',
      version='0.1',
      description='Extract text from PDF documents easily.',
      author='Tim McNamara',
      author_email='paperless@timmcnamara.co.nz',
      keywords=('pdf', 'text', 'text-extraction'),
      license = "GPL v3 or later",
      packages=['slate'],
      package_dir={'slate': 'src/slate'},
      requires=['pdfminer'],
      classifiers= [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Topic :: Office/Business',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Text Processing',
        'Topic :: Utilities'],
      long_description = """Slate is a Python package that simplifies the process of extracting
text from PDF files. It depends on the PDFMiner package.

Slate provides one class, PDF. PDF takes a file-like object and
will extract all text from the document, presentating each page
as a string of text:

  >>> with open('example.pdf') as f:
  ...    doc = slate.PDF(f)
  ...
  >>> doc[1]
  'Text from page 2...'

If your pdf is password protected, pass the password as the
second argument:

  >>> with open('secrets.pdf') as f:
  ...     doc = slate.PDF(f, 'password')
  ...
  >>> doc[0]
  "My mother doesn't know this, but..." """)
