from django.conf.urls import url
from django.views.generic import TemplateView

from .views import asistencia, registro

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="pase_lista/index.html"), name='index'),
    url(r'^asistencia/(?P<alumno>\d+)/$', asistencia, name='asistencia'),
    url(r'^registro/$', registro, name='registro'),
]