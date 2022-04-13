from django.urls import path 

from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('slang/', views.slang_index, name='index'),
  path('slang/<int:slang_id>/', views.slang_detail, name='detail'),
  path('slang/create/', views.SlangCreate.as_view(), name='slang_create'),
  path('slang/<int:pk>/update/', views.SlangUpdate.as_view(), name='slang_update'),
  path('slang/<int:pk>/delete/', views.SlangDelete.as_view(), name='slang_delete'), 
]


