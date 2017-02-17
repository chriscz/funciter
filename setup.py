import os
import sys

from setuptools import setup, find_packages

VERSION = '0.2.0'

setup(
    name='funciter',
    version=VERSION,
    description='Functional style iterators and iterable manipulation',
    #long_description=open(os.path.join(base_dir, 'description.txt')).read().strip(),
    license='Mozilla Public License 2.0 (MPL 2.0)',
    url='https://github.com/chriscz/pyfuncty',

    author='Chris Coetzee',
    author_email='chriscz93@gmail.com',

    #packages=find_packages(),
    modules=["funciter"],
    include_package_data=True,
    zip_safe=False,

    classifiers=[]
)
