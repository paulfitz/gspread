#!/usr/bin/env python

import os.path
import re
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

def read(filename):
    return open(os.path.join(os.path.dirname(__file__), filename)).read()

description = 'Tiny gspread fork to support public spreadsheets'

long_description = """
A tweaked version of gspread:
  * Supports public, published spreadsheets.
  * Preserves unset cell values as null versus ''.

All credit for gspread to Anton Burnashev fuss.here@gmail.com and others,
this is just a tiny fork.

License
-------
MIT

"""

long_description = long_description.lstrip("\n")

version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                    read('gspread/__init__.py'), re.MULTILINE).group(1)

setup(
    name='gspread_public',
    packages=['gspread'],
    description=description,
    long_description=long_description,
    version=version,
    author='Paul Fitzpatrick',
    author_email='paulfitz@alum.mit.edu',
    url='https://github.com/paulfitz/gspread',
    keywords=['spreadsheets', 'google-spreadsheets'],
    install_requires=['requests>=2.2.1'],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Science/Research",
        "Topic :: Office/Business :: Financial :: Spreadsheet",
        "Topic :: Software Development :: Libraries :: Python Modules"
        ],
    license='MIT'
    )
