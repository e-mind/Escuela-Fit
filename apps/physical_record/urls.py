from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^$', record_list, name='list'),
    url(r'^create/$', RecordCreate.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/$', RecordDetail.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/delete/$', RecordDelete.as_view(), name='delete'),
    url(r'^(?P<pk>\d+)/update/$', RecordUpdate.as_view(), name='update'),
]