from django.contrib.auth.models import User

from django import forms
from .models import *




class InsertQuestions(forms.ModelForm):
	class Meta:
		model = Question
		fields = '__all__'
		exclude = ['exam']


class AddExam(forms.ModelForm):
	class Meta:
		model = Exam
		fields = '__all__'
		exclude = ['total_marks']