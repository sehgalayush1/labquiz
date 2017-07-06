# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import pdb
from django.db import models
from teacher.models import Exam,Question

class Test(models.Model):
	Test_exam = models.ForeignKey(Exam)

	def __unicode__(self):
		return self.Test_exam.name
	

# Create your models here.
class Ques(models.Model):
	Test_question = models.ForeignKey(Question)

	
	def __unicode__(self):	
		return self.Test_question.question