# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone
import datetime
# Create your models here.

# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')
#
#
# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)

@python_2_unicode_compatible
class Shop(models.Model):
	shop_name = models.CharField(max_length=200)
	update_date = models.DateTimeField('Date Updated')

	def __str__(self):
		return self.shop_name

	def was_update_recently(self):
		return self.update_date >= timezone.now() - datetime.timedelta(days=1)

@python_2_unicode_compatible
class Comment(models.Model):
	shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
	comment_text = models.CharField(max_length=200)
	author = models.IntegerField(default=0)

	def __str__(self):
		return self.comment_text