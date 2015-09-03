`Package Documentation`_

Description
===========

This package provides decorators to make building websites in Django
even easier.

Installation
============

.. code:: console

    $ pip install django-decorator-plus

Basic Usage
===========

The package currently supplies decorators to improve your views.

The ``require_http_methods()`` decorator is an enhanced version of the
`decorator supplied by Django`_.

.. code:: python

    @require_http_methods(["GET", "POST"])
    def function_view(request):
        # HTTP methods != GET or POST results in 405 error code response

The ``require_http_methods()`` automatically supplies the ``OPTIONS`` HTTP
method, and will automatically add the ``HEAD`` HTTP method if the
``GET`` method is allowed.

The package also supplies two shortcut decorators for your most common
tasks:

- ``require_safe_methods`` limits views to ``GET`` and ``HEAD``.
- ``require_form_methods`` limites views to ``GET``, ``HEAD``, and
  ``POST``.

.. _`decorator supplied by Django`: https://docs.djangoproject.com/en/stable/topics/http/decorators/#django.views.decorators.http.require_http_methods
.. _`Package Documentation`: https://django-decorator-plus.readthedocs.org
