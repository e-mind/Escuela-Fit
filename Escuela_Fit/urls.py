from django.contrib import admin
from django.conf.urls import url, include
from django.views.generic import TemplateView

urlpatterns = [
	# MAIN
    url(r'^$', TemplateView.as_view(template_name='main/index.html'), name='index'),
    url(r'^login/$', TemplateView.as_view(template_name='main/login.html'), name='login'),
    # url(r'^logout/$', , name='logout'),
    url(r'^nutrition/$', TemplateView.as_view(template_name='main/nutrition.html'), name='nutrition'),
    url(r'^profile/$', TemplateView.as_view(template_name='main/profile.html'), name='profile'),
    url(r'^signup/$', TemplateView.as_view(template_name='main/signup.html'), name='signup'),
    url(r'^weather/$', TemplateView.as_view(template_name='main/weather.html'), name='weather'),
    url(r'^workout/$', TemplateView.as_view(template_name='main/workout.html'), name='workout'),

    # APPS
    url(r'^admin/', admin.site.urls),
    url(r'^attendance/', include('apps.attendance.urls', namespace='attendance')),
    url(r'^students/', include('apps.students.urls', namespace='students')),
]