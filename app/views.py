from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('<h1>WELCOME TO HOMEPAGE</h1>')

def sam(request):
    return render(request,"sample.html")

