=====================
Django Decorator Plus
=====================

.. image:: http://img.shields.io/pypi/status/django-decorator-plus.svg
    :target: https://pypi.python.org/pypi/django-decorator-plus
.. image:: http://img.shields.io/pypi/v/django-decorator-plus.svg
    :target: https://pypi.python.org/pypi/django-decorator-plus
.. image:: https://img.shields.io/pypi/pyversions/django-decorator-plus.svg
    :target: https://pypi.python.org/pypi/django-decorator-plus
.. image:: https://img.shields.io/badge/Django-1.7%2C%201.8-brightgreen.svg
    :target: https://pypi.python.org/pypi/django-decorator-plus

.. image:: https://readthedocs.org/projects/django-decorator-plus/badge/?version=latest
    :target: https://django-decorator-plus.readthedocs.org
    :alt: Documentation Statu

Description
===========

This package provides decorators to make building websites in Django
even easier.

Installation
============

.. code:: console

    $ pip install django-decorator-plus

Usage
=====

Please see the `Package Documentation`_ for all usage information. The
`PYPI`_ page has a basic demonstration of a few of the more notable
decorators in the package.

Contributing
============

Please fork the project to your own github account, create a new branch
for your feature or fix, and then pull request any changes.

Any changes to the code must be reflected in the documentation.

To run tests, please first install the development copy of the project
in your environment (use of |virtualenvwrapper|_ encouraged). This may
be accomplished with |pip|_.

.. code:: console

    $ # from the project root directory
    $ pip install -e .

Tests may then be run thanks to the ``Makefile``.

.. code:: console

    $ make test

.. _`Package Documentation`: https://django-decorator-plus.readthedocs.org
.. _`PyPI`: https://pypi.python.org/pypi/django-decorator-plus
.. |pip| replace:: ``pip``
.. _`pip`: https://pypi.python.org/pypi/pip
.. |virtualenvwrapper| replace:: ``virtualenvwrapper``
.. _`virtualenvwrapper`: https://pypi.python.org/pypi/virtualenvwrapper
