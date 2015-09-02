# -*- coding: utf-8 -*-
"""
=======================================
Django Decorator Plus Setuptools Module
=======================================

:website: https://github.com/jambonrose/django-decorator-plus
:copyright: Copyright 2015 Andrew Pinkham
:license: Simplified BSD, see LICENSE for details.
"""
from __future__ import unicode_literals

from setuptools import setup, find_packages
from codecs import open
from os.path import abspath, dirname, join

PROJECT_DIR = abspath(dirname(__file__))

with open(join(PROJECT_DIR, 'DESCRIPTION.rst'), encoding='utf-8') as f:
    long_description = f.read()

version = {}
init_file = join(PROJECT_DIR, 'decorator_plus', '__init__.py')
with open(init_file, encoding='utf-8') as f:
    exec(f.read(), version)

setup(
    name='django-decorator-plus',
    version=version['__version__'],

    keywords=['django', 'decorator', 'http'],
    description='Extra decorators for your Django project.',
    long_description=long_description,

    url='https://github.com/jambonrose/django-decorator-plus',

    author='Andrew Pinkham',
    author_email='hello at andrewsforge dot com',

    license='Simplified BSD License',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Framework :: Django :: 1.4',
        'Framework :: Django :: 1.5',
        'Framework :: Django :: 1.6',
        'Framework :: Django :: 1.7',
        'Framework :: Django :: 1.8',
    ],

    packages=find_packages(exclude=['docs', 'tests', 'requirements']),
)
