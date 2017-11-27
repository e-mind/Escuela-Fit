from django.conf.urls import url, include
from django.contrib import admin

from .views import list, create, detail

urlpatterns = [
    url(r'^$', list, name='list'),
    url(r'^create/(?:(?P<schedule>\w+)/)?$', create, name='create'),
    url(r'^(?P<schedule>\w+)/(?P<pk>\d+)/?$', detail, name='detail'),
]
