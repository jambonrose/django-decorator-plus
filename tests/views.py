from django.http import HttpResponse

from decorator_plus import require_http_methods


@require_http_methods(['GET'])
def function_view_limit_get(request):
    return HttpResponse('Hello World!')


@require_http_methods(['post'])
def function_view_limit_post(request):
    return HttpResponse('Hello World!')
