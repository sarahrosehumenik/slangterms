from django.shortcuts import render

from .models import Slang

# Create your views here.
from django.http import HttpResponse 



def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def slang_index(request):
    slangterms = Slang.objects.all()
    return render(request, 'slang/index.html', {"slangterms": slangterms})