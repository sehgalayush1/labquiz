# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.models  import User
from teacher.models import Exam,Question
from django.http import *

def dashboard(request):
	if request.user.is_authenticated():
		exam = Exam.objects.all()
		return render(request, 'student/exam_list.html', {'exam': exam})
	else:
		return HttpResponseRedirect('/')

def allQuestions(request, id):
	if request.user.is_authenticated():
		exam = Exam.objects.get(pk=id)
		if request.method=='POST':
			count = Question.objects.filter(exam=exam).count()
			quess = Question.objects.filter(exam=exam)
			for i in range(count):
				ques_id = quess[i].id
				name = 'op_' + str(ques_id)
				print ques_id
				responses = request.POST.getlist(ques_id)
				print responses
				print request.POST
			return HttpResponse('success')
		else:
			return render(request, 'student/questions.html', {'exam': exam})
	else:
		return HttpResponseRedirect('/')
