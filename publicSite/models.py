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
    amount_available = models.IntegerField()

    def email(self):
        return self.user.email
    email.boolean = False
    email.short_description = 'Email'

    def location(self):
        return self.city + ', ' + self.state
    location.boolean = False
    location.short_description = 'Location'
    location.admin_order_field = 'city'

    def amount_available_display(self):
        return '$%d' % self.amount_available
    amount_available_display.short_description = 'Can provide'
    amount_available_display.admin_order_field = 'amount_available'

    def money_display(self):
        return self.money
    money_display.short_description = 'Willing to give ($)'
    money_display.admin_order_field = 'money'
    money_display.boolean = True

    def travel_display(self):
        return self.travel
    travel_display.short_description = 'Willing to drive (🚘)'
    travel_display.admin_order_field = 'travel'
    travel_display.boolean = True

    def has_match(self):
        return len(self.match_set.all()) != 0
    has_match.short_description = 'Has been matched?'
    has_match.boolean = True

class Helpee(models.Model):
    user = models.OneToOneField(User, related_name='helpee')

    info = models.BooleanField()
    state = models.CharField(max_length=20)
    city = models.CharField(max_length=60)

    travel = models.BooleanField()
    money = models.BooleanField()
    amount_needed = models.IntegerField()
    travel_cost = models.IntegerField()

    def email(self):
        return self.user.email
    email.boolean = False
    email.short_description = 'Email'
    email.admin_order_field = 'user'

    def location(self):
        return self.city + ', ' + self.state
    location.boolean = False
    location.short_description = 'Location'
    location.admin_order_field = 'city'

    def money_display(self):
        return self.money
    money_display.short_description = 'Needs money?'
    money_display.admin_order_field = 'money'
    money_display.boolean = True

    def amount_needed_display(self):
        return '$%d' % self.amount_needed
    amount_needed_display.short_description = 'Needs'
    amount_needed_display.admin_order_field = 'amount_needed'

    def travel_display(self):
        return self.travel
    travel_display.short_description = 'Needs transportation?'
    travel_display.admin_order_field = 'travel'
    travel_display.boolean = True

    def travel_cost_display(self):
        return '$%d' % self.travel_cost
    travel_cost_display.short_description = 'Needs'
    travel_cost_display.admin_order_field = 'travel_cost'

    def info_display(self):
        return self.info
    info_display.short_description = 'Has questions?'
    info_display.admin_order_field = 'info'
    info_display.boolean = True

    def has_match(self):
        return len(self.match_set.all()) != 0
    has_match.short_description = 'Has been matched?'
    has_match.boolean = True

class Demographic(models.Model):
    user = models.OneToOneField(User, related_name="demographics")

    age_category = models.IntegerField()
    gender = models.CharField(max_length=255)
    ethnicity = models.CharField(max_length=255)

class Match(models.Model):
    helper = models.ForeignKey(Helper, on_delete=models.CASCADE)
    helpee = models.ForeignKey(Helpee, on_delete=models.CASCADE)

    match_type = models.CharField(max_length=1, choices=(('t', 'travel'), ('m', 'money')))
    estimated_dollars = models.IntegerField()

    def helper_email(self):
        return self.helper.user.email
    helper_email.boolean = False
    helper_email.short_description = 'Helper Email'

    def helpee_email(self):
        return self.helpee.user.email
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
