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

    def email(self):
        return self.user.email
    email.boolean = False
    email.short_description = 'Email'

    def location(self):
        return self.city + ', ' + self.state
    location.boolean = False
    location.short_description = 'Location'

    def availability(self):
        available = []
        if self.travel:
            available.append('travel')
        if self.money:
            available.append('money')
        return ', '.join(available)
    availability.boolean = False
    availability.short_description = 'Availability'

class Helpee(models.Model):
    user = models.OneToOneField(User, related_name='helpee')

    info = models.BooleanField()
    state = models.CharField(max_length=20)
    city = models.CharField(max_length=60)

    travel = models.BooleanField()
    money = models.BooleanField()

    def email(self):
        return self.user.email
    email.boolean = False
    email.short_description = 'Email'

    def location(self):
        return self.city + ', ' + self.state
    location.boolean = False
    location.short_description = 'Location'

    def needs(self):
        needs = []
        if self.info:
            needs.append('info')
        if self.travel:
            needs.append('travel')
        if self.money:
            needs.append('money')
        return ', '.join(needs)
    needs.boolean = False
    needs.short_description = 'Needs'

class Demographic(models.Model):
    user = models.OneToOneField(User, related_name="demographics")

    age_category = models.IntegerField()
    gender = models.CharField(max_length=255)
    ethnicity = models.CharField(max_length=255)

class Match(models.Model):
    helper = models.ForeignKey(User, on_delete=models.CASCADE, related_name='%(class)s_helper')
    helpee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='%(class)s_helpee')

    match_type = models.CharField(max_length=1, choices=(('t', 'travel'), ('m', 'money')))
    estimated_dollars = models.IntegerField()

    def helper_email(self):
        return self.helper.email
    helper_email.boolean = False
    helper_email.short_description = 'Helper Email'

    def helpee_email(self):
        return self.helpee.email
    helpee_email.boolean = False
    helpee_email.short_description = 'Helpee Email'

    # helper_review = Review.objects.get(match=self, user=helper)
    # helpee_review = Review.objects.get(match=self, user=helpee)

class Review(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    rating = models.IntegerField()
    details = models.TextField()

    actual_dollars = models.IntegerField()
