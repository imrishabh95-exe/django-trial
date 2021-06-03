from home.models import Contact
from django.http.response import HttpResponse
from django.shortcuts import render
from datetime import datetime
from django.contrib.messages import constants as messages
from django.contrib import messages

# Create your views here.
def index(request):
    context = {
        'variable':'This is sent',
    }
    messages.success(request, 'This is a test message')
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    if request.method == 'POST':
        name  = request.POST.get('name')
        email  = request.POST.get('email')
        phone  = request.POST.get('phone')
        desc  = request.POST.get('desc')

        contact = Contact(name=name, email=email, phone=phone, desc=desc, date= datetime.today())
        contact.save()
        messages.success(request, 'You message sent')
    return render(request, 'contact.html')