# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse, HttpResponseRedirect ,Http404
from django.shortcuts import render
from django.contrib.auth.models  import User
from .models import *

# Create your views here.

def exam_list(request):
	if request.user.is_authenticated():
		Student_exam= Test.objects.all()
		
		return render(request, 'student/list.html', {'Student_exam': Student_exam})
	else:
		return HttpResponseRedirect('/')

