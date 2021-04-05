from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index2(request):
    return HttpResponse('<h1>WELCOME TO HOMEPAGE of app2</h1>')

def sam2(request):
    return render(request,"sample.html")

def ren2(request):
    return render(request,'sample_app2.html')