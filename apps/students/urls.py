from django.conf.urls import url, include

from .views import *

urlpatterns = [
    # Student's URLs
    url(r'^$', student_list, name='list'),
    url(r'^create/$', StudentCreate.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/$', StudentDetail.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/delete/$', StudentDelete.as_view(), name='delete'),
    url(r'^(?P<pk>\d+)/update/$', StudentUpdate.as_view(), name='update'),

    # Physical Records URLs
    url(r'^(?:(?P<student>\d+/)?)record/', include('apps.physical_record.urls', namespace='record')),
]