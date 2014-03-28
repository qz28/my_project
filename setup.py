#! /usr/bin/env python

import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "microbiosima",
    version = "0.0.4",
    author = "qz and js and sw",
    author_email = "",
    description = (""),
    license = "BSD",
    keywords = "",
    url = "",
    packages=['microbiosima',],
    package_dir={'microbiosima': 'microbiosima'},
    test_suite = "microbiosima.test",
    long_description=read('README.txt'),
    classifiers=[
    ],
)