from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('<h1>WELCOME TO HOMEPAGE OF APP1</h1>')

def sam1(request):
    return render(request,"html_app1/sample1.html")

def ren1(request):
    return render(request,'sample_app1.html')

