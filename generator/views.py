from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    return render(request, 'generator/home.html', {'password': 'jdkfjkd932ksk'})

def password(request):
    
    thepassword = ''

    characters = list('qwertyuiopasdfghjklzxcvbnm')
    length = int(request.GET.get('length'))

    if request.GET.get('uppercase'):
        characters.extend(list('QWERTYUIOPASDFGHJKLZXCVBNM'))

    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))

    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*(){[}]?'))

    for x in range(length):
        thepassword += random.choice(characters)

    return  render(request, 'generator/password.html', {'password':thepassword})

def about(request):
    return render(request, 'generator/about.html')
