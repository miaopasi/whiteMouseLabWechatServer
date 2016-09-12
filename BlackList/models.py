# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone
import datetime
# Create your models here.



@python_2_unicode_compatible
class Shop(models.Model):
	"""
	Need To Add:
	shop_webid: Link to Dianping,etc.
	shop_location: Position of Shop.
	...
	According to Data Structure Got. Also Should Update Admin Part.
	"""
	shop_name = models.CharField(max_length=200)
	update_date = models.DateTimeField('Date Updated')

	def __str__(self):
		return self.shop_name

	def was_update_recently(self):
		now = timezone.now()
		return (now - datetime.timedelta(days=1) <= self.update_date <= now)

@python_2_unicode_compatible
class Comment(models.Model):
	"""
	According to Scrawler Data.Should add something.
	"""
	shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
	comment_text = models.CharField(max_length=200)
	author = models.IntegerField(default=0)

	def __str__(self):
		return self.comment_text