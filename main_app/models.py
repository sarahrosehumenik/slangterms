from django.db import models

from django.urls import reverse

class React(models.Model):
  reaction = models.CharField(max_length=50)
  

  def __str__(self):
    return self.reaction

  def get_absolute_url(self):
    return reverse('reactions_detail', kwargs={'pk': self.id})


class Slang(models.Model):
  term = models.CharField(max_length=100)
  definition = models.CharField(max_length=500)
  example = models.CharField(max_length=500)
  reactions = models.ManyToManyField(React)
  
  def __str__(self): 
   return self.term
 
  def get_absolute_url(self):
   return reverse('detail', kwargs={'slang_id': self.id })

class Thesaurus(models.Model):
  synonym = models.CharField(max_length=100)
  antonym = models.CharField(max_length=100)

  slang = models.ForeignKey(Slang, on_delete=models.CASCADE)

  def __str__(self): 
   return self.synonym


  