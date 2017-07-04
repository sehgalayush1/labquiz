# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class StudentProfile(models.Model):
	user = models.OneToOneField(User)
	year = models.IntegerField(blank=True, null=True)
	branch = models.CharField(max_length=100,blank=True, null=True)
	mobile = models.CharField(max_length=10, blank=True, null=True)
	timestamp = models.DateTimeField(auto_now=True,auto_now_add=False)
	total_score = models.IntegerField(default=0)

	def __unicode__(self):
		return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        StudentProfile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.studentprofile.save()