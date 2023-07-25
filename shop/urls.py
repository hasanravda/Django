from django.contrib import admin
from django.urls import path
from shop import views
from .models import Product

urlpatterns = [
    path('', views.index,name='Home'),
    path('collection/', views.collection,name='Collection'),
    path('kurti/', views.kurti,name='category_kurti'),
]