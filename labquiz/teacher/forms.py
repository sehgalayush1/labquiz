from django.contrib.auth.models import User

from django import forms
from .models import *


answerChoices = (
    (1, ('option1')),
    (2, ('option2')),
    (3, ('option3')),
    (4, ('option4')),
    )

class InsertQuestions(forms.ModelForm):
	answer = forms.ChoiceField(choices=answerChoices, widget=forms.RadioSelect())
	class Meta:
		model = Question
		fields = '__all__'
		exclude = ['exam']


class AddExam(forms.ModelForm):
	class Meta:
		model = Exam
		fields = '__all__'
		exclude = ['total_marks']