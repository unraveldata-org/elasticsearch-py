# -*- coding: utf-8 -*-
from os.path import join, dirname
from setuptools import setup, find_packages
import sys

VERSION = (5, 5, 3)
__version__ = VERSION
__versionstr__ = '.'.join(map(str, VERSION))

f = open(join(dirname(__file__), 'README'))
long_description = f.read().strip()
f.close()

install_requires = [
    'urllib3>=1.21.1',
]
tests_require = [
    'requests>=2.0.0, <3.0.0',
    'nose',
    'coverage',
    'mock',
    'pyaml',
    'nosexcover'
]


setup(
    name = 'elasticsearch-unravel',
    description = "Python client for Elasticsearch",
    license="Apache License, Version 2.0",
    url = "https://github.com/elastic/elasticsearch-py",
    long_description = long_description,
    version = __versionstr__,
    author = "venkatesh",
    author_email = "pvenkatesh@unraveldata.com",
    packages=find_packages(
        where='.',
        exclude=('test_elasticsearch*', )
    ),
    classifiers = [
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: Apache Software License",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
    install_requires=install_requires,

    test_suite='test_elasticsearch.run_tests.run_all',
    tests_require=tests_require,

    extras_require={
        'develop': tests_require + ["sphinx", "sphinx_rtd_theme"]
    },
)
