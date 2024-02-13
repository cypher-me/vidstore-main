from django.contrib import admin
from django.urls import path
from .views import StoreListView, StoreDetailView
from . import views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', views.index, name='store-index'),
    path('about/', views.about, name='store-about'),
    path('store/', login_required(StoreListView.as_view()), name='store-store'),
    path('store/<int:pk>/', StoreDetailView.as_view(), name='store-detail'),
]

