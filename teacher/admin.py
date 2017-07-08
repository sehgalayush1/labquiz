# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *
# Register your models here.

class PostModelAdmin(admin.ModelAdmin): #customizing admin
	list_display = ["question"]
	
	list_filter = ["question"] #filter the fields
	search_fields = ["question"] #search the fields
	#list_editable = ["question"] #we can edit the fields like here title
	class Meta:
		model = Question #adding post model to PostAdmin

admin.site.register(Exam)
admin.site.register(Question,PostModelAdmin)