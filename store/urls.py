from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='store-index'),
    path('about/', views.about, name='store-about'),
    path('store/', views.store, name='store-store'),
]

