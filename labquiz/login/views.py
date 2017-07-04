# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import auth
from django.shortcuts import render
from django.http import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models  import User
from .forms import *
from .models import *

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


def auth_view_student(request):
	pass


def logout(request):
	auth.logout(request)
	return HttpResponseRedirect('/')


def register(request):
	if request.method=="POST":
		form = StudentForm(request.POST)
		if form.is_valid():
			# form.save()
			username = form.cleaned_data.get('username')
			email = form.cleaned_data.get('email')
			password = form.cleaned_data.get('password1')
			year = form.cleaned_data.get('year')
			branch = form.cleaned_data.get('branch')
			mobile = form.cleaned_data.get('mobile')
			user = User.objects.create_user(username=username, password=password, email=email)
			user.studentprofile.year = year
			user.studentprofile.branch = branch
			user.studentprofile.mobile = mobile
			user.save()
			return render(request, 'login/register_success.html', {'name': request.POST['username']})
			# return HttpResponseRedirect('/')
	else:
		form = StudentForm()
	return render(request, 'login/register.html', {'form':form})