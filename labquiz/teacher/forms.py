from django.contrib.auth.models import User

from django import forms
from .models import *



class UserForm(forms.ModelForm):
	password =forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model = User
		fields = ['username','email','password']


class InsertQuestions(forms.ModelForm):
	class Meta:
		model = Question
		fields = ('question', 'option1', 'option2', 'option3', 'option4', 'answer')


class AddExam(forms.ModelForm):
	class Meta:
		model = Exam
		fields = '__all__'