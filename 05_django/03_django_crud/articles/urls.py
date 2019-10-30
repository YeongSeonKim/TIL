from django.urls import path
from . import views

urlpatterns = [
    path('<int:article_pk>/', views.detail),
    path('create/', views.create),
    path('new/', views.new),
    path('', views.index),
]
