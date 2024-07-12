from django.shortcuts import render,redirect
from django.http import HttpResponse

def home(request):
    return render(request,"home.html")


def contract(request):
    return HttpResponse("Thin is my contract page")

def about(request):
    return render(request,"about.html")