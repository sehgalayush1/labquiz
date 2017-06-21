from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', index),
    url(r'^addExam/$', addExam, name = 'addExam'),
    url(r'^addQuestion/$', addQuestion, name = 'addQuestion'),
    url(r'^allQuestions/(\d+)/$', allQuestions, name = 'allQuestions'),
    url(r'^editQuestion/(\d+)/$', editQuestion, name = 'editQuestion'),
    
]