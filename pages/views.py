from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    return HttpResponse("Home Page")


def communitacion(request):
    return HttpResponse("Communication")


def aboutUs(request):
    return HttpResponse("About US")
