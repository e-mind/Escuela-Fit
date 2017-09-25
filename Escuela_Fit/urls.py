from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
	# MAIN
    url(r'^$', TemplateView.as_view(template_name='main/index.html'), name='index'),
    url(r'^login/$', TemplateView.as_view(template_name='main/iniciars.html'), name='login'),
    # url(r'^logout/$', , name='logout'),
    url(r'^rutina/$', TemplateView.as_view(template_name='main/rutina.html'), name='rutina'),
    url(r'^dieta/$', TemplateView.as_view(template_name='main/nutricion.html'), name='dieta'),
    url(r'^calidad_aire/$', TemplateView.as_view(template_name='main/ca.html'), name='calidad_aire'),
    url(r'^perfil/$', TemplateView.as_view(template_name='main/perfil.html'), name='perfil'),

    # APPS
    url(r'^admin/', admin.site.urls),
    url(r'^pase_lista/', include('apps.pase_lista.urls', namespace='pase_lista')),
    url(r'^alumnos/', include('apps.alumnos.urls', namespace='alumnos')),
]