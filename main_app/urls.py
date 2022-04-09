from django.urls import path 

from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('slang/', views.slang_index, name='index'),
]


