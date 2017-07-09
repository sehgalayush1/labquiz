# -*- coding: utf-8 -*-
from __future__ import unicode_literals



from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import *
from .models import *
from django.http import *
from django.contrib.auth import authenticate,login
from django.contrib.auth import logout
from django.views import generic
from django.views.generic import View
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models  import User



# Create your views here.
examId = 0
def index(request):
	if request.user.is_authenticated():
		exam = Exam.objects.all()

		return render(request, 'teacher/home.html', {'exam': exam})
	else:
		return HttpResponseRedirect('/')


def addExam(request):
	if request.user.is_authenticated():
		if request.method == "POST":
			form = AddExam(request.POST)
			if form.is_valid():
				form.save()
				return HttpResponseRedirect('/teacher/')
		else:
			form = AddExam()
		return render(request, 'teacher/addExam.html', {'form':form})
	else:
		return HttpResponseRedirect('/')


def addQuestion(request):
	if request.user.is_authenticated():
		if request.method == "POST":
			form = InsertQuestions(request.POST)
			if form.is_valid():
				f = form.save(commit= False)
				f.exam = Exam.objects.get(pk=examId)
				f.save()
				messages.success(request, 'New question added!')
				return HttpResponseRedirect(reverse_lazy('teacher:addQuestion')) #needs to be redirected to the previous page where more can be added easily.
			else:
				return render(request, 'error.html')
		form = InsertQuestions()
		return render(request, 'teacher/insertQues.html',{'form': form})
	else:
		return HttpResponseRedirect('/')



def allQuestions(request, id):
	if request.user.is_authenticated():
		exam = Exam.objects.get(pk=id)
		global examId
		examId = id
		return render(request, 'teacher/displayques.html', {'exam': exam})
	else:
		return HttpResponseRedirect('/')


def editQuestion(request, id):
	if request.user.is_authenticated():
		n = Question.objects.get(id=id)
		if request.method == "POST":
			form = InsertQuestions(request.POST,instance=n)
			if form.is_valid():
				form.save()
				exam = Exam.objects.get(pk=id)
				return render(request, 'teacher/displayques.html', {'exam': exam})
		else:
			form = InsertQuestions(instance=n)
		return render(request,'teacher/editQues.html', {'form': form})
	else:
		return HttpResponseRedirect('/')


def addStaff(request):
	if request.user.is_authenticated():
		if request.method=='POST':
			username = request.POST['username']
			password = request.POST['password']

			user = User.objects.create_user(username = username, password = password)
			user.save()
			return HttpResponseRedirect('/teacher/addStaff/')
		else:
			users = User.objects.all()
		return render(request, 'teacher/addStaff.html',{'users': users})
	else:
		return HttpResponseRedirect('/')
