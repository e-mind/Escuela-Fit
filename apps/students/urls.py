from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required

from .views import *

urlpatterns = [
    # Student's URLs
    url(r'^$', student_list, name='list'),
    url(r'^create/$', login_required(StudentCreate.as_view()), name='create'),
    url(r'^(?P<pk>\d+)/$', login_required(StudentDetail.as_view()), name='detail'),
    url(r'^(?P<pk>\d+)/delete/$', login_required(StudentDelete.as_view()), name='delete'),
    url(r'^(?P<pk>\d+)/update/$', login_required(StudentUpdate.as_view()), name='update'),
]
