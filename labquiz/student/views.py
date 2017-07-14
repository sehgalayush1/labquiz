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


def exam(request, exam_name):
	'''
	View renders all the questions of an exam in a template and handles
	the response sent by the user after taking the exam.
	'''
	# Handle the uninvited guests
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/')

	# Fetch the exam passed in url from db
	exam = Exam.objects.get(name=exam_name)

	# Handle the response data
	if request.method == 'POST':
		questions = exam.question_set.all()
		answers = {}
		
		# Store all the user's answers in a dictionary
		for question in questions:
			answers[question.question] = request.POST.getlist(question.question)
		print answers
		# Check answers and calculate the score
		score = 0
		marks_per_question = exam.marks_per_question
		negative_marks = exam.negative_marks
		for question in questions:
			print question.answer[0]
			if int(answers[question.question] == question.answer):
				score += marks_per_question
			elif(answers[question.question] == []):
				pass
			else:
				score -= negative_marks
		
		return HttpResponse(score)
	
	# Display all the questions to the user
	context = { 'exam': exam }
	return render(request, 'student/show_questions.html', context)