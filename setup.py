#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='slate',
      version='0.2.3',
      description='Extract text from PDF documents easily.',
      author='Tim McNamara',
      author_email='paperless@timmcnamara.co.nz',
      keywords=('pdf', 'text', 'text-extraction'),
      license = "GPL v3 or later",
      exclude_package_data={'': ['.gitignore']},
      packages=find_packages('src'),
      package_dir={'': 'src'},
      requires=['pdfminer'],
      install_requires=['distribute'],
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
      long_description = open('README').read(),
      url='http://pypi.python.org/pypi/slate')
