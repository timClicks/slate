#!/usr/bin/env python

from setuptools import setup, find_packages

import sys
PYTHON_3 = sys.version_info[0] == 3
if PYTHON_3:
    pdfminer = 'pdfminer3k'
else:
    pdfminer = 'pdfminer'

with open('README') as f:
    long_description = f.read()

setup(name='slate',
      version='0.5.2',
      description='Extract text from PDF documents easily.',
      author='Tim McNamara',
      author_email='paperless@timmcnamara.co.nz',
      keywords=('pdf', 'text', 'text-extraction'),
      license = "MIT License",
      exclude_package_data={'': ['.gitignore']},
      packages=find_packages('src'),
      package_dir={'': 'src'},
      requires=[pdfminer],
      install_requires=['setuptools', pdfminer],
      classifiers= [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Topic :: Office/Business',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Text Processing',
        'Topic :: Utilities'],
      long_description=long_description,
      url='http://github.com/timClicks/slate')
