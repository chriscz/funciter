import os
import sys

from setuptools import setup, find_packages

VERSION = '0.2.2'

setup(
    name='funciter',
    version=VERSION,
    description='Functional style iterators and iterable manipulation',
    license='Mozilla Public License 2.0 (MPL 2.0)',
    url='https://github.com/chriscz/funciter',

    author='Chris Coetzee',
    author_email='chriscz93@gmail.com',

    #packages=find_packages(),
    py_modules=["funciter"],
    include_package_data=True,
    zip_safe=False,

    classifiers=[]
)
