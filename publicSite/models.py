# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
 
class Helper(models.Model):
    user = models.OneToOneField(User, related_name='helper')
 
    state = models.CharField(max_length=20)
    city = models.CharField(max_length=60)

    travel = models.BooleanField()
    money = models.BooleanField()

class Helpee(models.Model):
    user = models.OneToOneField(User, related_name='helpee')

    info = models.BooleanField()
    state = models.CharField(max_length=20)
    city = models.CharField(max_length=60)

    travel = models.BooleanField()
    money = models.BooleanField()

class Demographic(models.Model):
    user = models.OneToOneField(User, related_name="demographics")

    age_category = models.IntegerField()
    gender = models.CharField(max_length=255)
    ethnicity = models.CharField(max_length=255)
