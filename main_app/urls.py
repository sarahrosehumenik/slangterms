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
  path('slang/<int:slang_id>/add_thesaurus/', views.add_thesaurus, name='add_thesaurus'), 
  path('slang/<int:slang_id>/assoc_reaction/<int:reaction_id>/', views.assoc_reaction, name='assoc_reaction'),
  path('slang/<int:slang_id>/unassoc_reaction/<int:reaction_id>/', views.unassoc_reaction, name='unassoc_reaction'),
  path('reactions/', views.ReactList.as_view(), name='reactions_index'),
  path('reactions/<int:pk>/', views.ReactDetail.as_view(), name='reactions_detail'),
  path('reactions/create/', views.ReactCreate.as_view(), name='reactions_create'),
  path('reactions/<int:pk>/update/', views.ReactUpdate.as_view(), name='reactions_update'),
  path('reactions/<int:pk>/delete/', views.ReactDelete.as_view(), name='reactions_delete'),
]


