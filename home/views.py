from django.shortcuts import render,HttpResponse
from .models import Plateform,Certificate,Skills,MyProjects

def index(request):
    return render(request,'index.html')

def plateform(request):
    plateforms=Plateform.objects.all()
    return render(request,'plateform.html',{'plateforms':plateforms})


def about(request):
    skills=Skills.objects.all()
    return render(request,'about.html',{'skills':skills})

def services(request):
    certificates=Certificate.objects.all()
    return render(request,'services.html',{'certificates':certificates})

