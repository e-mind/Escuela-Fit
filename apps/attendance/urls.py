from django.conf.urls import url
from django.views.generic import TemplateView

from .views import index, register

urlpatterns = [
    url(r'^(?P<student>\d+)/$', index, name='index'),
    url(r'^register/$', register, name='register'),
]