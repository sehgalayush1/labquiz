from django.conf.urls import url, include
from django.views.generic import TemplateView
from .views import *

urlpatterns = [
    url(r'^$', dashboard, name = 'dashboard'),
    url(r'^allQuestions/(\d+)/$', allQuestions, name = 'allQuestions'),
]
