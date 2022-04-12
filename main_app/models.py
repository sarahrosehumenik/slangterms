from django.db import models


class Slang(models.Model):
  term = models.CharField(max_length=100)
  definition = models.CharField(max_length=500)
  example = models.CharField(max_length=500)

  def __str__(self): 
   return self.term