from django.forms import ModelForm
from .models import Thesaurus

class ThesaurusForm(ModelForm):
  class Meta:
    model = Thesaurus
    fields = ['synonym', 'antonym']