from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^limit-get/$', views.function_view_limit_get, name='limit-get'),
    url(r'^limit-post/$', views.function_view_limit_post, name='limit-post'),
    url(r'^limit-safe/$', views.function_view_limit_safe, name='limit-safe'),
]
