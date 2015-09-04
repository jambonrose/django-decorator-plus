====================
View Decorator Usage
====================

The package currently supplies decorators to improve your views.

.. contents::
    :local:
    :depth: 1

Controlling HTTP Methods in Function Views
==========================================

The view decorators provided are meant to restrict the HTTP methods
allowed on a view. At the base of all of these decorators is the
``require_http_methods()`` decorator , which is an enhanced version of
the `decorator supplied by Django`_ by the same name.

.. code-block:: python

    from decorator_plus import require_http_methods

    @require_http_methods(["GET", "POST"])
    def function_view(request):
        # The site will respond with an HTTP 405 error code if 
        # the HTTP method is not: GET, HEAD, POST, OPTIONS

The ``require_http_methods()`` (in this package, not Django's)
automatically supplies the ``OPTIONS`` HTTP method, and will
automatically add the ``HEAD`` HTTP method if the ``GET`` method is
allowed.

The package also supplies two shortcut decorators for your most common
tasks:

- ``require_safe_methods`` limits views to ``GET`` and ``HEAD`` (and
  ``OPTIONS``),
- ``require_form_methods`` limits views to ``GET``, ``HEAD``, and
  ``POST`` (and ``OPTIONS``)

.. code-block:: python

    from decorator_plus import (
        require_form_methods,
        require_safe_methods,
    )

    @require_form_methods
    def function_view_form(request):
        # equivalent to :
        # @require_http_methods(["GET", "HEAD", "POST"])

    @require_safe_methods
    def function_view_safe(request):
        # equivalent to :
        # @require_http_methods(["GET", "HEAD"])

.. _`decorator supplied by Django`: https://docs.djangoproject.com/en/stable/topics/http/decorators/#django.views.decorators.http.require_http_methods
