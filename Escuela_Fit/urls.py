from django.conf.urls import url, include
from django.contrib import admin
from .views import index

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^pase_lista/', include('apps.pase_lista.urls', namespace='pase_lista')),
    url(r'^alumnos/', include('apps.alumnos.urls', namespace='alumnos')),
]