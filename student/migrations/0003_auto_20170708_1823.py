# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-08 18:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_auto_20170706_0811'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ques',
            name='Test_question',
        ),
        migrations.RemoveField(
            model_name='test',
            name='Test_exam',
        ),
        migrations.DeleteModel(
            name='Ques',
        ),
        migrations.DeleteModel(
            name='Test',
        ),
    ]
