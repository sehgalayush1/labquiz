# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .forms import *
from .models import *
from django.http import *

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
	return HttpResponseRedirect('/teacher/')


def allQuestions(request, id):
	exam = Exam.objects.get(pk=id)
	return render(request, 'teacher/displayques.html', {'exam': exam})
