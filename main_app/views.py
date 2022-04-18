from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Slang, React




from .forms import ThesaurusForm

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
  reactions = React.objects.exclude(id__in=slang.reactions.all().values_list('id'))
  thesaurus_form = ThesaurusForm()

  return render(request, 'slang/detail.html', { 'slang': slang, 'thesaurus_form': thesaurus_form, 'reactions': reactions })

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

def add_thesaurus(request, slang_id):
  # create a ModelForm instance using the data in the posted form
    form = ThesaurusForm(request.POST)
  # validate the data
    if form.is_valid():
      new_thesaurus = form.save(commit=False)
      new_thesaurus.slang_id = slang_id
      new_thesaurus.save()
    return redirect('detail', slang_id=slang_id)

class ReactList(ListView):
  model = React

class ReactDetail(DetailView):
  model = React

class ReactCreate(CreateView):
  model = React
  fields = '__all__'

class ReactUpdate(UpdateView):
  model = React
  fields = ['reaction']

class ReactDelete(DeleteView):
  model = React
  success_url = '/reactions/'

def assoc_reaction(request, slang_id, reaction_id):
  Slang.objects.get(id=slang_id).reactions.add(reaction_id)
  return redirect('detail', slang_id=slang_id)

def unassoc_reaction(request, slang_id, reaction_id):
  Slang.objects.get(id=slang_id).reactions.remove(reaction_id)
  return redirect('detail', slang_id=slang_id)