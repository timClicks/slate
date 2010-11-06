#!/usr/bin/env python

from distutils.core import setup
from sys import version
if version < '2.2.3':
    from distutils.dist import DistributionMetadata
    DistributionMetadata.classifiers = None
    DistributionMetadata.download_url = None


setup(name='slate',
      version='0.2.2',
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
      long_description = open('README').read())
