# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponseRedirect, HttpResponse

from django.core.urlresolvers import reverse
from django.shortcuts import render

from publicSite.models import Helper, Helpee, Demographic

# Create your views here.
def index(request):
    return render(request, 'index.html')



#NEW - show form to create new helper
def getHelperForm(request):
    return render(request, 'helperForm.html')

#CREATE - add new helper to database
def submitHelperInfo(request):

    user = request.user

    try:
        helper = user.helper
    except:
        helper = Helper(user = user)
    
    selections = request.POST.getlist('checks[]')
    
    helper.money = 'money' in selections 
    helper.travel = 'travel' in selections
    helper.save()

    return HttpResponseRedirect(reverse('getDemographicForm'))

  
  
#NEW - show form to create new helpee
def getHelpeeForm(request):
    return render(request, "helpeeForm.html")
    
#CREATE - add new helpee to database
def submitHelpeeInfo(request):

    user = request.user
    
    try:
        helpee = user.helpee
    except:
        helpee = Helpee(user = user)
    
    selections = request.POST.getlist('checks[]')
    
    helpee.info = 'info' in selections
    helpee.money = 'money' in selections 
    helpee.travel = 'travel' in selections
    helpee.save()

    return HttpResponseRedirect(reverse('getDemographicForm'))




#NEW - show form to create new location
def getLocationForm(request):
    return render(request, 'locationForm.html')
    
#CREATE - add new campground to database
def submitLocationInfo(request):
    return



#NEW - show form to create new demographic info
def getDemographicForm(request):
    return render(request, 'demographicForm.html')
   
#CREATE - add new demographic info to database
def submitDemographicInfo(request):
    
    return
    
