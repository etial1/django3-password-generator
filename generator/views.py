from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.


def home(request):
    return render(request, 'generator/home.html')


def about(request):
    return render(request, 'generator/about.html')


def password(request):
    # uppercase
    # numbers
    # special
    abc = list('abcdefghijklmnopqrstuvwxyz')
    len = int(request.GET.get('lenght'))
    gpassword=''

    if request.GET.get('uppercase'):
        abc.extend(list(item.upper() for item in abc))
    if request.GET.get('numbers'):
        abc.extend(list('0123456789'))
    if request.GET.get('special'):
        abc.extend(list('!@#$%^&*()_+'))
    for x in range(len):
        gpassword += random.choice(abc)

    return render(request, 'generator/password.html', {'password': gpassword})
