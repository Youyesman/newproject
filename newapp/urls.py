from unicodedata import name
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index , name='index'),
    path('searchplayer',views.searchplayer,name='searchplayer'),
    path('updateplayer/<int:id>',views.updateplayer,name='updateplayer'),
    path('deleteplayer/<int:id>',views.deleteplayer,name='deleteplayer'),
    path('plus/<int:id>',views.plus,name='plus'),
    path('minus/<int:id>',views.minus,name='minus'),
]
