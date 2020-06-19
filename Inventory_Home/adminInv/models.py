# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class User(models.Model):
    username = models.CharField(max_length=30, unique='True')
    sesskey = models.CharField(max_length=50)
    fullName = models.CharField(max_length=50)
    role = models.CharField(max_length=30)
    password =  models.CharField(max_length=30)
