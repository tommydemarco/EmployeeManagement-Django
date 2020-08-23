"""
EMPLOYEES URLS
"""
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    #LIST VIEWS
    path('list-all/', views.ListAllEmployees.as_view(), name="list_all"),
    path('list-by-field/<str:fieldname>', views.ListEmployeesByField.as_view(), name="list_by_field"),
    path('list-by-keyword/', views.ListEmployeesByKeyword.as_view(), name="list_by_keyword"),
    #DETAIL VIEWS
    path('employee-details/<pk>', views.EmployeeDetails.as_view(), name="employee_details"),
    #CREATE VIEWS
    path('add-new-employee/', views.CreateNewEmployee.as_view(), name="new_employee"),

    
]