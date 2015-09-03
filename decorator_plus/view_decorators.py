import logging
from functools import wraps

from django.core.exceptions import ImproperlyConfigured
from django.http import HttpResponse, HttpResponseNotAllowed
from django.utils.decorators import available_attrs

logger = logging.getLogger('django.request')


HTTP_METHOD_NAMES = (
    'CONNECT',
    'DELETE',
    'GET',
    'HEAD',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
    'TRACE',
)


def require_http_methods(request_methods):
    """
    Decorator to make a function view only accept particular request methods.
    Usage::

        @require_http_methods(["GET", "POST"])
        def function_view(request):
            # HTTP methods != GET or POST results in 405 error code response
    """
    if not isinstance(request_methods, (list, tuple)):
        raise ImproperlyConfigured(
            "require_http_methods decorator must be called "
            "with a list or tuple of strings. For example:\n\n"
            "    @require_http_methods(['GET', 'POST'])\n"
            "    def function_view(request):\n"
            "        ...\n")

    request_methods = list(map(str.upper, request_methods))

    for method in request_methods:
        if method not in HTTP_METHOD_NAMES:
            raise ImproperlyConfigured(
                "require_http_method called with '%s', "
                "which is not a valid HTTP method.\n"
                % (method,))

    if 'GET' in request_methods and 'HEAD' not in request_methods:
        request_methods.append('HEAD')
    if 'OPTIONS' not in request_methods:
        request_methods.append('OPTIONS')
    request_methods.sort()

    def decorator(func):
        @wraps(func, assigned=available_attrs(func))
        def inner(request, *args, **kwargs):
            if request.method == 'OPTIONS':
                response = HttpResponse()
                response['Allow'] = ', '.join(
                    [m.upper() for m in request_methods])
                response['Content-Length'] = '0'
                return response
            if request.method not in request_methods:
                logger.warning(
                    'Method Not Allowed (%s): %s',
                    request.method,
                    request.path,
                    extra={
                        'status_code': 405,
                        'request': request
                    }
                )
                return HttpResponseNotAllowed(request_methods)
            return func(request, *args, **kwargs)
        return inner
    return decorator


require_safe_methods = require_http_methods(["GET", "HEAD"])
require_safe_methods.__doc__ = (
    "Decorator to require that a function view only accept safe methods: "
    "GET and HEAD.")


require_form_methods = require_http_methods(["GET", "HEAD", "POST"])
require_form_methods.__doc__ = (
    "Decorator to require that a function view only accept "
    "GET, HEAD and POST methods.")
