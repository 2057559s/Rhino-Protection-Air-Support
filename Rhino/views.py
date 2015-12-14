__author__ = 'nicholassaunderson'

__author__ = 'nicholassaunderson'
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    response = render(request,'index.html')
    return response

def home(request):
    response = render(request,'home.html')
    return response