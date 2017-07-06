from django.conf.urls import url, include
from django.views.generic import TemplateView
from .views import *

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name = 'login/home.html')),
    url(r'^exam_list/$', exam_list, name = 'exam_list'),
    url(r'^allQuestions/(\d+)/$', allQuestions, name = 'allQuestions'),
]
