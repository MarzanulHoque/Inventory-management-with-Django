# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class User(models.Model):
    uid = models.CharField(max_length=10)
    sesskey = models.CharField(max_length=50)
    fullName = models.CharField(max_length=50)
    role = models.CharField(max_length=30)
    password =  models.CharField(max_length=30)
