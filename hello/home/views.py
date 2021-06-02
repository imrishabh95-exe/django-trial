from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse('This is home page')

def about(request):
    return HttpResponse('This is about page')

def services(request):
    return HttpResponse('This is service page')