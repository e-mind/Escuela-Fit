from django.contrib import admin
from django.conf.urls import url, include
from django.views.generic import TemplateView

from .views import weather, index, activation_complete, profile

urlpatterns = [
	# MAIN
    url(r'^$', index, name='index'),
    url(r'^profile/$', profile, name='profile'),
    url(r'^weather/$', weather, name='weather'),
    url(r'^news/$', TemplateView.as_view(template_name="main/notips.html"), name='news'),
    url(r'^tips/$', TemplateView.as_view(template_name="main/tipsA.html"), name='tips'),
    url(r'^es_sano_hacer_una_sola_comida_al_dia/$', TemplateView.as_view(template_name="main/es_sano_hacer_una_sola_comida_al_dia.html"), name='new1'),

    # APPS
    url(r'^admin/', admin.site.urls),
    url(r'^attendance/', include('apps.attendance.urls', namespace='attendance')),
    url(r'^nutrition/', include('apps.nutrition.urls', namespace='nutrition')),
    url(r'^students/', include('apps.students.urls', namespace='students')),
    url(r'^record/', include('apps.physical_record.urls', namespace='record')),

    # 3rd party
    url(r'^accounts/activate/complete/$', activation_complete, name='registration_activation_complete'),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^social/', include('social_django.urls', namespace='social'))
]
