from django.conf.urls import url, include
from django.contrib import admin

from .views import list, create, detail, cancel, update_food

urlpatterns = [
    url(r'^$', list, name='list'),
    url(r'^cancel/$', cancel, name='cancel'),
    url(r'^create/(?:(?P<schedule>\w+)/)?$', create, name='create'),
    url(r'^(?P<schedule>\w+)/(?P<pk>\d+)/$', detail, name='detail'),
    url(r'^(?P<key>\w+)/(?P<nf_pk>\d+)/update/$', update_food, name='update_food'),
]
