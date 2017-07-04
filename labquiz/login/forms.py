
from django import forms
from .models import *


class StudentForm(forms.ModelForm):
	username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), max_length = 30, required = True)
	email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control'}), max_length = 30, required = True)
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}), max_length = 30, required = True)
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}),	max_length = 30, required = True)
	year = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), max_length = 30, required = True)
	branch = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), max_length = 30, required = True)
	mobile = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), max_length = 30, required = True)
	#for converting Char into Password Field
	
	def clean_username(self):
		n = self.cleaned_data['username']
		try:
			match = User.objects.get(username__iexact=n)
		except:
			return self.cleaned_data['username']
		raise forms.ValidationError("username already exist!")

	def clean_email(self):
		mail = self.cleaned_data['email']
		try:
			match = User.objects.get(email__iexact=mail)
		except:
			return self.cleaned_data['email']
		raise forms.ValidationError("already email exist")


	def clean(self):
		if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
			if self.cleaned_data['password1'] != self.cleaned_data['password2']:
				raise forms.ValidationError('password doesn\'t match')
			return self.cleaned_data

	class Meta:
		model = StudentProfile
		fields = ['username','email','password1', 'password2', 'year', 'branch', 'mobile']

