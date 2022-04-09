from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse 


def home(request):
    return HttpResponse('<h1>hello daddy</h1>')

def about(request):
    return HttpResponse('<h1>about</h1>')

def index(request):
    return HttpResponse('<h1>all the slang terms</h1>')