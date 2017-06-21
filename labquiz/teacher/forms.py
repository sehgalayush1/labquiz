from django import forms
from .models import *


class InsertQuestions(forms.ModelForm):
	class Meta:
		model = Question
		fields = '__all__'


class AddExam(forms.ModelForm):
	class Meta:
		model = Exam
		fields = '__all__'