from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse 

class Slang:
  def __init__(self, term, definition, example):
      self.term = term
      self.definition = definition
      self.example = example
    
slangterms = (
    Slang("Disney Adult", "A millenial adult,with or without kids, that can't stop talking about disney", "Raul is a Disney Adult"),
    Slang("Wife guy", "A man who takes any opportunity to mention his wife", "raul is a wife guy"),
    Slang("Hose Sniffer", "A person who hangs around firefighters with the intent of satisfying personal relationship desires", "raul is a hose sniffer")
)

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def slang_index(request):
    return render(request, 'slang/index.html')