"""
EMPLOYEES URLS
"""
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('list-all/', views.ListAllEmployees.as_view(), name="list_all"),
    path('list-by-field/<str:fieldname>', views.ListEmployeesByField.as_view(), name="list_by_field"),
    path('list-by-keyword/', views.ListEmployeesByKeyword.as_view(), name="list_by_keyword"),
    
]