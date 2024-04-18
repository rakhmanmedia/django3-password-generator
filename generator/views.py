from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

# Function to create range of char
def range_char(first, last):
    return (chr(n) for n in range(ord(first), ord(last) + 1))

def home(request):
    return render(request, 'generator/home.html')

def password(request):

    the_password = ''

    length = int(request.GET.get('length'))

    characters = list(range_char("a", "z"))

    if request.GET.get('uppercase'):
        characters.extend(list(range_char("A", "Z")))

    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*(){[}]?'))
 
    similars = ('0,O,o L,l,i,1')

    for x in range(length):
        the_password += random.choice(characters)

        if request.GET.get('similar'):
            while True:
                if similars.find(the_password[-1]) > 0:
                    the_password = the_password[:-1]
                    the_password += random.choice(characters)
                else:
                    break
                

    return HttpResponse(the_password)

def about(request):
    return render(request, 'generator/about.html')
