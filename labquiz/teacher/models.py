# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from multiselectfield import MultiSelectField

# Create your models here.

answerChoices = (
    (1, ('option1')),
    (2, ('option2')),
    (3, ('option3')),
    (4, ('option4')),
    )

class Exam(models.Model):
    name = models.CharField(max_length=100,default="")
    marks_per_question = models.IntegerField(default=1)
    negative_marks = models.IntegerField(default = 0)
    total_marks = models.IntegerField(default = 0, null=True, blank=True)

    def __unicode__(self):
        return self.name


class Question(models.Model):
    question = models.TextField(max_length=200,default="")
    option1 = models.CharField(max_length=50,default="")
    option2 = models.CharField(max_length=50, default="")
    option3 = models.CharField(max_length=50, default="")
    option4 = models.CharField(max_length=50, default="")
    answer = MultiSelectField(choices=answerChoices, null=False, blank=False,max_choices=1)
    exam = models.ForeignKey(Exam)

    def __unicode__(self):
        return self.question