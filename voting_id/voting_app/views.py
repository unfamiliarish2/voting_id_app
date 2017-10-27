from __future__ import unicode_literals
from django.shortcuts import render

def index(request):
	context={}
	return render(request, 'voting_app/index.html', context)