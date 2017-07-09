# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse, HttpResponseRedirect ,Http404
from django.shortcuts import render
from django.contrib.auth.models  import User
from .models import *


from teacher.models import Exam,Question

examId = 0
def exam_list(request):
	if request.user.is_authenticated():
		exam = Exam.objects.all()

		return render(request, 'student/dashboard.html', {'exam': exam})
	else:
		return HttpResponseRedirect('/')

def allQuestions(request, id):
	if request.user.is_authenticated():
		exam = Exam.objects.get(pk=id)
		global examId
		examId = id
		return render(request, 'student/question.html', {'exam': exam})
	else:
		return HttpResponseRedirect('/')
