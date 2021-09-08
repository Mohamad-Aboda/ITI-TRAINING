from django.contrib import admin
from django.urls.conf import path
from . import views
urlpatterns = [
    path('', views.index, name='index'), 
    path('home/', views.home, name='home'), 
    path('about/', views.about, name='about'), 
    path('contact/', views.contact, name='contact'),
    path('search/', views.search, name='search'),
    path('add/', views.add, name='add'),
    path('update/', views.update, name='update'),
    path('delete/', views.delete, name='delete'),
    path('add/added', views.added, name='added'),


]
