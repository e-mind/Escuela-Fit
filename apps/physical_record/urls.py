from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .views import *

urlpatterns = [
    url(r'^$', record_list, name='list'),
    url(r'^create/(?:(?P<student>\d+)/)?$', login_required(RecordCreate.as_view()), name='create'),
    url(r'^(?P<pk>\d+)/delete/$', login_required(RecordDelete.as_view()), name='delete'),
    url(r'^(?P<pk>\d+)/update/$', login_required(RecordUpdate.as_view()), name='update'),
]
