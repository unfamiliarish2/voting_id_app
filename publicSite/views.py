# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse

from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')


#NEW - show form to create new helper
def getHelperForm(request):
    return render(request, 'helperForm.html')
    
#CREATE - add new helper to database
def submitHelperInfo(request):
    return 


'''
#NEW - show form to create new helpee
def getHelpeeForm(request):
    return render(request, "helpeeForm.html")
    
#CREATE - add new helpee to database
def sumbitHelpeeInfo(request, "")


#NEW - show form to create new location
def getLocationForm(request):
    return render(request, "")
    
#CREATE - add new campground to database
def submitLocationInfo(request, "")


#NEW - show form to create new demographic info
def getDemographicForm(request):
    return render(request, "")
    
#CREATE - add new demographic info to database
def submitDemographicInfo(request, "")

'''
