from django.shortcuts import render,HttpResponse
from .models import Plateform,Certificate,Skills,MyProjects

def plateform(request):
    plateforms=Plateform.objects.all()
    return render(request,'plateform.html',{'plateforms':plateforms})


def index(request):
    projects=MyProjects.objects.all()
    skills=Skills.objects.all()
    return render(request,'index.html',{'skills':skills,'projects':projects})

def services(request):
    certificates=Certificate.objects.all()
    return render(request,'services.html',{'certificates':certificates})

