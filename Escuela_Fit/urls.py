from django.contrib import admin
from django.conf.urls import url, include
from django.views.generic import TemplateView

from .views import weather, index, MyActivationView

urlpatterns = [
	# MAIN
    url(r'^$', index, name='index'),
    url(r'^profile/$', TemplateView.as_view(template_name='main/profile.html'), name='profile'),
    url(r'^weather/$', weather, name='weather'),

    # APPS
    url(r'^admin/', admin.site.urls),
    # url(r'^attendance/', include('apps.attendance.urls', namespace='attendance')),
    # url(r'^students/', include('apps.students.urls', namespace='students')),
    url(r'^accounts/activate/complete/$', MyActivationView.as_view(), name='registration_activation_complete'),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^nutrition/', include('apps.nutrition.urls', namespace='nutrition')),
    url(r'^social/', include('social_django.urls', namespace='social'))
]
