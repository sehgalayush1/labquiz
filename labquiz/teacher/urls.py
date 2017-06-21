from django.conf.urls import url
from .views import *
from . import views



urlpatterns = [
    url(r'^$', index , name='index'),
    url(r'^addExam/$', addExam, name = 'addExam'),
    url(r'^addQuestion/$', addQuestion, name = 'addQuestion'),
    url(r'^allQuestions/(\d+)/$', allQuestions, name = 'allQuestions'),
    url(r'^editQuestion/(\d+)/$', editQuestion, name = 'editQuestion'),
    url(r'^register/$' , views.UserFormView.as_view() , name = 'register' ), 
    url(r'^register/$', views.register, name='register'),

    
]