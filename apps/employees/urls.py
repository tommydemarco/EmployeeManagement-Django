"""
EMPLOYEES URLS
"""
from django.contrib import admin
from django.urls import path

from . import views

#giving an app name
app_name = "employees_app"

urlpatterns = [
    #LIST VIEWS
    path('', views.ListAllEmployees.as_view(), name="list_all"),
    path('list-by-field/<str:fieldname>', views.ListEmployeesByField.as_view(), name="list_by_field"),
    path('name-search/', views.ListEmployeesByKeyword.as_view(), name="name_search"),
    #DETAIL VIEWS
    path('employee-details/<pk>', views.EmployeeDetails.as_view(), name="employee_details"),
    #CREATE VIEWS
    path('add-new-employee/', views.CreateNewEmployee.as_view(), name="add_new_employee"),
    #UPDATE VIEWS
    path('update-employee/<pk>', views.UpdateEmployee.as_view(), name="update_employee"),
    #DELETE VIEWS
    path('delete-employee/<pk>', views.DeleteEmployee.as_view(), name="delete_employee"),
    #TEMPLATE VIEWS
    path('contact-support/', views.ContactSupport.as_view(), name="contact_support"),
    
]