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

View Decorators
---------------

The view decorators provided are meant to restrict the HTTP methods
allowed on a view. The ``require_safe_methods`` limits views to ``GET``
and ``HEAD`` and generates a proper response for ``OPTIONS``.

.. code-block:: python

    from decorator_plus import require_safe_methods

    @require_safe_methods
    def function_view_safe(request):
        ...

The package also supplies the ``require_form_methods`` decorator, which
limits views to ``GET``, ``HEAD``, and ``POST``. Both of these
decorators are actually just shortcuts on top of the
``require_http_methods()`` decorator, which is an enhanced version of
the `decorator supplied by Django`_ by the same name; the
``require_http_methods()`` decorator automatically supplies the
``OPTIONS`` HTTP method, and will automatically add the ``HEAD`` HTTP
method if the ``GET`` method is allowed.

For more information and examples, please see the full `Package
Documentation`_.

.. _`decorator supplied by Django`: https://docs.djangoproject.com/en/stable/topics/http/decorators/#django.views.decorators.http.require_http_methods
.. _`Package Documentation`: https://django-decorator-plus.readthedocs.org
