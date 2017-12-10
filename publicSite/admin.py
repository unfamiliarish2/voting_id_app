# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from publicSite.models import Helper, Helpee, Demographic, Match, Review

class HelperAdmin(admin.ModelAdmin):
    fields = ['user', 'city', 'state', 'travel', 'money', 'amount_available']
    list_display = ['email', 'location', 'travel_display', 'money_display', 'amount_available_display', 'has_match']

class HelpeeAdmin(admin.ModelAdmin):
    fields = ['user', 'state', 'city', 'info', 'travel', 'money', 'amount_needed']
    list_display = ['email', 'location', 'info_display', 'travel_display', 'money_display', 'amount_needed_display', 'has_match']

class DemographicAdmin(admin.ModelAdmin):
    fields = ['user', 'age_category', 'gender', 'ethnicity']

class MatchAdmin(admin.ModelAdmin):
    fields = ['helper', 'helpee', 'match_type', 'estimated_dollars']
    list_display = ['helper_email', 'helpee_email', 'match_type', 'estimated_dollars']

class ReviewAdmin(admin.ModelAdmin):
    fields = ['match', 'user', 'rating', 'details', 'actual_dollars']

admin.site.register(Helper, HelperAdmin)
admin.site.register(Helpee, HelpeeAdmin)
admin.site.register(Demographic, DemographicAdmin)
admin.site.register(Match, MatchAdmin)
admin.site.register(Review, ReviewAdmin)
