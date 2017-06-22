# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.shortcuts import render,redirect
from .forms import *
from .models import *
from django.http import *
from django.contrib.auth import authenticate,login
from django.contrib.auth import logout
from django.views import generic
from django.views.generic import View


# Create your views here.
def index(request):
	exam = Exam.objects.all()
	return render(request, 'teacher/home.html', {'exam': exam})


def addExam(request):
	if request.method == "POST":
		form = AddExam(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/teacher/')
	else:
		form = AddExam()
	return render(request, 'teacher/addExam.html', {'form':form})


def addQuestion(request):
	if request.method == "POST":
		form = InsertQuestions(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/teacher/')	#needs to be redirected to the previous page where more can be added easily.
	else:
		form = InsertQuestions()
	return render(request, 'teacher/insertQues.html',{'form':form})
	


def allQuestions(request, id):
	exam = Exam.objects.get(pk=id)
	return render(request, 'teacher/displayques.html', {'exam': exam})


def editQuestion(request, id):
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


class UserFormView(View):
	form_class = UserForm
	template_name = 'teacher/registration_form.html'

	def get(self, request): # get request method #display blank form
		form = self.form_class(None) #its none because user gets empty form
		return render(request, self.template_name, {'form' : form})
	def post(self, request): # post request method #procee form data into database
		form = self.form_class(request.POST)

		if form.is_valid():

			user = form.save(commit=False)

			#cleaned (normalized) data
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user.set_password(password)
			user.save()

			# returns user objects if credentials are correct
			user = authenticate(username=username, password=password) #verifies the entered credentials with that saved in database

			if user is not None:

				if user.is_active:
					login(request, user)
					return redirect('/teacher/') # after log in get them redirected to home page

		return render(request, self.template_name, {'form' : form})	

def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                
                return render(request, 'teacher/home.html')
    context = {
        "form": form,
    }
    return render(request, 'teacher/home.html', context)


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                
                return render(request, 'teacher/home.html')
            else:
                return render(request, 'teacher/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'teacher/login.html', {'error_message': 'Invalid login'})
    return render(request, 'teacher/login.html')

def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'teacher/login.html', context)