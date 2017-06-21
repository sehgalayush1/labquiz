from django.conf.urls import url
from django.contrib import admin
from . views import (
	ques_create,
	
	)

urlpatterns = [
	
    url(r'^create/$', ques_create),
    

]