from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^list/$', alumno_list, name='list'),
    url(r'^create/$', AlumnoCreate.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/$', AlumnoDetail.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/update/$', AlumnoUpdate.as_view(), name='update'),
    url(r'^(?P<pk>\d+)/delete/$', AlumnoDelete.as_view(), name='delete'),

    url(r'^fisicos/list/$', alumno_fisicos_list, name='list_fisicos'),
    url(r'^(?:(?P<pk>\d+/)?)fisicos/create/$', AlumnoFisicosCreate.as_view(), name='create_fisicos'),
    url(r'^(?P<pk>\d+)/fisicos/$', AlumnoFisicosDetail.as_view(), name='detail_fisicos'),
    url(r'^(?P<pk>\d+)/fisicos/update/$', AlumnoFisicosUpdate.as_view(), name='update_fisicos'),
    url(r'^(?P<pk>\d+)/fisicos/delete/$', AlumnoFisicosDelete.as_view(), name='delete_fisicos'),
]
