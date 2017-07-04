
from django.conf.urls import url, include
from django.views.generic import TemplateView
from .views import *

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name = 'login/home.html')),
    url(r'^auth/$', auth_view, name = 'check'),
    url(r'^auth_student/$', auth_view_student, name = 'checkstudent'),
    url(r'^register/$', register, name = 'register'),
    url(r'^invalid/$', TemplateView.as_view(template_name = 'login/invalid.html')),
    url(r'^logout/$', logout),


]
