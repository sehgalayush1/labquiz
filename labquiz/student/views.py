# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.models  import User
from teacher.models import Exam,Question
examId=0
def dashboard(request):
	if request.user.is_authenticated():
		exam = Exam.objects.all()
		return render(request, 'student/exam_list.html', {'exam': exam})
	else:
		return HttpResponseRedirect('/')

def allQuestions(request, id):
	if request.user.is_authenticated():
		exam = Exam.objects.get(pk=id)
		global examId
		examId = id
		return render(request, 'student/questions.html', {'exam': exam})
	else:
		return HttpResponseRedirect('/')
