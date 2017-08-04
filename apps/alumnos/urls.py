from django.conf.urls import url

from .views import AlumnoCreate, AlumnoList, AlumnoUpdate, AlumnoDetail, AlumnoDelete

urlpatterns = [
    url(r'^list/$', AlumnoList.as_view(), name='list'),
    url(r'^create/$', AlumnoCreate.as_view(), name='create'),
    url(r'^(?P<pk>[0-9]+)/$', AlumnoDetail.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/update/$', AlumnoUpdate.as_view(), name='update'),
    url(r'^(?P<pk>[0-9]+)/delete/$', AlumnoDelete.as_view(), name='delete'),
]