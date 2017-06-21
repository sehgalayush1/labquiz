# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from .models import Question
from .forms import QuesForm

# Create your views here.

def ques_create(request):
	form =QuesForm(request.POST or None, request.FILES or None) # request.FILES or None:for images
	if form.is_valid():
		instance = form.save(commit = False)
		instance.save()
		#message success
		
		 
	context={
		"form": form,
	}
	return render(request, "ques_form.html", context) 


