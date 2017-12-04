from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.decorators import login_required

from .views import list, create, detail, cancel, update_food, NutritionDelete

urlpatterns = [
    url(r'^$', list, name='list'),
    url(r'^cancel/$', cancel, name='cancel'),
    url(r'^create/(?:(?P<schedule>\w+)/)?$', create, name='create'),
    url(r'^(?P<schedule>\w+)/(?P<pk>\d+)/$', detail, name='detail'),
    url(r'^(?P<pk>\d+)/delete/$', login_required(NutritionDelete.as_view()), name='delete'),
    url(r'^(?P<key>\w+)/(?P<nf_pk>\d+)/update/$', update_food, name='update_food'),
]
