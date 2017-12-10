# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from publicSite.models import Helper, Helpee, Demographic

# Register your models here.

class HelperAdmin(admin.ModelAdmin):
    fields = ['user', 'state', 'city', 'info', 'travel', 'money']

class HelpeeAdmin(admin.ModelAdmin):
    fields = ['user', 'state', 'city', 'travel', 'money']

class DemographicAdmin(admin.ModelAdmin):
    fields = ['user', 'age_category', 'gender', 'ethnicity']



admin.site.register(Helper, HelperAdmin)
admin.site.register(Helpee, HelpeeAdmin) 
admin.site.register(Demographic, DemographicAdmin)