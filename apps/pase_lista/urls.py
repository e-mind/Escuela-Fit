from django.conf.urls import url
from django.views.generic import TemplateView

from .views import json_data

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="pase_lista/index.html"), name='index'),
    url(r'^json_data/$', json_data, name='json_data'),
]