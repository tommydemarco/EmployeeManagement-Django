"""
FIELDS URLS
"""
from django.contrib import admin
from django.urls import path

#importing the view
from . import views

urlpatterns = [
    path('prueba/', views.PruebaView.as_view()),
    
]