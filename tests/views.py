from django.http import HttpResponse

from decorator_plus import (
    require_form_methods, require_http_methods, require_safe_methods
)


@require_form_methods
def function_view_limit_form(request):
    return HttpResponse('Hello World!')


@require_http_methods(['GET'])
def function_view_limit_get(request):
    return HttpResponse('Hello World!')


@require_http_methods(['post'])
def function_view_limit_post(request):
    return HttpResponse('Hello World!')


@require_safe_methods
def function_view_limit_safe(request):
    return HttpResponse('Hello World!')
