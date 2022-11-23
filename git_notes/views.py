from django.shortcuts import render
from django.http import HttpResponse
from . import notebook.html

# Create your views here.
def index(request):
	return HttpResponse("")
