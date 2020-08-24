"""
FIELDS URLS
"""
from django.contrib import admin
from django.urls import path

from . import views as vs


app_name = "fields_app"

urlpatterns = [
    #EDIT VIEWS
    path('add-new-field', vs.NewFieldView.as_view(), name="add_new_field"),
]