# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from publicSite.models import Helper, Helpee, Demographic, Match, Review

# Register your models here.

class HelperAdmin(admin.ModelAdmin):
    fields = ['user', 'city', 'state', 'travel', 'money']
    list_display = ['email', 'availability', 'location']

class HelpeeAdmin(admin.ModelAdmin):
    fields = ['user', 'state', 'city', 'info', 'travel', 'money']
    list_display = ['email', 'needs', 'location']

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
