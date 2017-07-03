# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import auth
from django.shortcuts import render
from django.http import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models  import User
# from .forms import *
# from .models import *

# Create your views here.

def auth_view(request):
	username = request.POST['username']
	password = request.POST['password']
	user = auth.authenticate(username=username, password=password)
	if user is not None:
		auth.login(request, user)
	else:
		return HttpResponseRedirect('/invalid/')
	return HttpResponseRedirect('/teacher/')


def logout(request):
	auth.logout(request)
	return HttpResponseRedirect('/')