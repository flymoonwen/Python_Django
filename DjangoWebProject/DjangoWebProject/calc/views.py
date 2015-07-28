# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

import time


def add(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a) + int(b);
    return HttpResponse(str(c))

def home(request):
    return render(request, 'index.html')

def doc(request):
    return HttpResponse(str(time.time())) 