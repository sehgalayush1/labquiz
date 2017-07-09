from django.contrib.auth.models import User

from django import forms
from .models import *




class InsertQuestions(forms.ModelForm):
	class Meta:
		model = Question
		fields = ('question', 'option1', 'option2', 'option3', 'option4', 'answer')


class AddExam(forms.ModelForm):
	class Meta:
		model = Exam
		fields = '__all__'