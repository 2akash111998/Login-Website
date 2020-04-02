# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):
	name = models.CharField(max_length = 264)
	email = models.EmailField(max_length = 264, unique = True)

	def __str__(self):
		return self.name