from django.shortcuts import render,HttpResponse
from .models import Plateform,Certificate

def index(request):
    plateforms=Plateform.objects.all()
    return render(request,'index.html',{'plateforms':plateforms})

def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')

def contact(request):
    return render(request,'contact.html')