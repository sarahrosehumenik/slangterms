from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView

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

def slang_detail(request, slang_id):
  slang = Slang.objects.get(id=slang_id)
  return render(request, 'slang/detail.html', { 'slang': slang })

class SlangCreate(CreateView):
  model = Slang
  fields = '__all__'
#you can use all or you can specify what fields in a list
class SlangUpdate(UpdateView):
  model = Slang
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = ['term', 'definition', 'example']

class SlangDelete(DeleteView):
  model = Slang
  success_url = '/slang/'