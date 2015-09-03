from django.core.exceptions import ImproperlyConfigured
from django.http import HttpResponse
from test_plus import TestCase

from decorator_plus import require_http_methods


class DecoratorTests(TestCase):

    def test_require_http_methods_configure(self):
        with self.assertRaises(ImproperlyConfigured):
            @require_http_methods('nope')
            def function_view_string_err(request):
                return HttpResponse('Nope')
        with self.assertRaises(ImproperlyConfigured):
            @require_http_methods(['CANHAS'])
            def function_view_no_such_method(request):
                return HttpResponse('Nope')

    def test_require_http_methods_form(self):
        url_name = 'limit-form'
        url = self.reverse(url_name)

        self.get_check_200(url_name)
        response = self.client.head(url)
        self.response_200(response)
        response = self.client.options(url)
        self.response_200(response)
        self.post(url_name)
        self.response_200()

        response = self.client.delete(url)
        self.response_405(response)
        response = self.client.patch(url)
        self.response_405(response)
        response = self.client.put(url)
        self.response_405(response)
        if hasattr(self.client, 'trace'):
            self.client.trace(url)
            self.response_405(response)

    def test_require_http_methods_get(self):
        url_name = 'limit-get'
        url = self.reverse(url_name)

        self.get_check_200(url_name)
        response = self.client.head(url)
        self.response_200(response)
        response = self.client.options(url)
        self.response_200(response)

        response = self.client.delete(url)
        self.response_405(response)
        response = self.client.patch(url)
        self.response_405(response)
        self.post(url_name)
        self.response_405()
        response = self.client.put(url)
        self.response_405(response)
        if hasattr(self.client, 'trace'):
            self.client.trace(url)
            self.response_405(response)

    def test_require_http_methods_post(self):
        url_name = 'limit-post'
        url = self.reverse(url_name)

        self.post(url_name)
        self.response_200()
        response = self.client.options(url)
        self.response_200(response)

        self.get(url_name)
        self.response_405()
        response = self.client.delete(url)
        self.response_405(response)
        response = self.client.head(url)
        self.response_405(response)
        response = self.client.patch(url)
        self.response_405(response)
        response = self.client.put(url)
        self.response_405(response)
        if hasattr(self.client, 'trace'):
            self.client.trace(url)
            self.response_405(response)

    def test_require_http_methods_safe(self):
        url_name = 'limit-safe'
        url = self.reverse(url_name)

        self.get_check_200(url_name)
        response = self.client.head(url)
        self.response_200(response)
        response = self.client.options(url)
        self.response_200(response)

        response = self.client.delete(url)
        self.response_405(response)
        response = self.client.patch(url)
        self.response_405(response)
        self.post(url_name)
        self.response_405()
        response = self.client.put(url)
        self.response_405(response)
        if hasattr(self.client, 'trace'):
            self.client.trace(url)
            self.response_405(response)
