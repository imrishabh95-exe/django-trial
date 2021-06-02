from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'variable':'This is sent',
    }
    return render(request, 'index.html', context) #render template
    #return HttpResponse('This is home page')

def about(request):
    return render(request, 'about.html') #render template
    #return HttpResponse('This is about page')

def services(request):
    return render(request, 'services.html') #render template
    #return HttpResponse('This is service page')

def contact(request):
    return render(request, 'contact.html') #render template
    #return HttpResponse('This is service page')