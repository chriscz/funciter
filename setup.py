import os
import sys

from setuptools import setup, find_packages

VERSION = '0.0.1'

setup(
    name='functy',
    version=VERSION,
    description='Functional iterator implementation',
    #long_description=open(os.path.join(base_dir, 'description.txt')).read().strip(),
    license='Apache License, Version 2.0',
    url='https://github.com/chriscz/pyfuncty',

    author='Chris Coetzee',
    author_email='chriscz93@gmail.com',

    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,

    classifiers=[
        "Development Status :: 1 - Planning",
        "License :: OSI Approved :: Apache Software License",
        "Topic :: Utilities",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
    ]
)
