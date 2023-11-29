from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('<h1> hi there </h1>')

# Create your views here.
