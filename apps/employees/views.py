from django.shortcuts import render

#import the list view 
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView, 
    TemplateView, 
    UpdateView,
    DeleteView,
)

#importing reverse lazy
from django.urls import reverse_lazy

#importing the model that is required in the class views
from .models import Employee

#importing the custom forms
from .forms import *

#creating the view that lists all employees
class ListAllEmployees(ListView):
    template_name = 'employees/list-all.html'
    model = Employee 
    #defining the name with which you'll be accessing the elements returned by the DB
    context_object_name = "employees"
    #adding pagination 
    paginate_by = 4
    #ordering results alphabetically by the first name 
    ordering = 'first_name'

class ListEmployeesByField(ListView):
    template_name = 'employees/list-by-field.html'
    context_object_name = "employees"
    #returning only the objects that have a centain attribute, a filter

    #making the query set the right way
    def get_queryset(self):

        #accessing the parameter passed in the URL (with str() and upper() for safety)
        field_filter = str(self.kwargs['fieldname']).upper()

        #now actually filtering for that variable
        filtered_list = Employee.objects.filter(
            field__alt_name = field_filter
        )

        #returning the filtered element list
        return filtered_list
    

#class based views for searching employees
class ListEmployeesByKeyword(ListView):
    template_name = 'employees/list-by-keyword.html'
    context_object_name = "employees"

    #making the query set the right way to display employees by keyword
    def get_queryset(self):

        #getting the keyword from the url
        first_name  = self.request.GET.get("first_name", '')
        last_name   = self.request.GET.get("last_name", '')

        #returning the search by first name 
        if first_name:

            filtered_list = Employee.objects.filter(
                first_name = first_name
            )

            return filtered_list

        #returning the search by last name 
        if last_name:

            filtered_list = Employee.objects.filter(
                last_name = last_name
            )

            if filtered_list.count() > 0: 

                return filtered_list

            else:
                no_results = "no results"
                return no_results

        #returning an empty list in case of no search
        return []

        
"""Start of the Detail Views"""
class EmployeeDetails(DetailView):
    template_name = "employees/employee-details.html"
    model = Employee

    #you don't need to specify which obkect you need the details of,
    #the DetailView knows it from the moment you pass the pk from the url

    #access the object returned in the template with the word object: {{ object }}

    #getting extra contex in the template with the method get_context_data
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["notice"] = "Notice: addresses should be verified witht the employees"

        #this for example would pass to the detail view a querySet of all the employees
        #context["notice"] = Employee.objects.all()

        return context
    

#CreeateView section

#create view for the insertion of a new employee
class CreateNewEmployee(CreateView):
    template_name = "employees/new-employee.html"
    model = Employee
    
    #inserting a form class for the form
    form_class = CreateEmployee

    #adding the url for when the process is complete.
    #required in a CreateView
    #syntax: 'urls_app_name:url_name'
    success_url = reverse_lazy('employees_app:creation_success')

    #THE FORM VALID  TAKES PLACE AFTER THE FORM HAS BEEN VALIDATED
    #adding attributes automatically using the method form_valid
    def form_valid(self, form):
        #saving the information submitted
        employee = form.save()
        #making the new attruibute to the new instance
        employee.full_name = employee.first_name + ' ' + employee.last_name
        #saving the outcome
        employee.save()

        #syntax for returning the result  of the form valid
        return super(CreateNewEmployee, self).form_valid(form)

    
#UptateView section
class UpdateEmployee(UpdateView):
    template_name = "employees/update-employee.html"
    model = Employee
    fields = fields = ['first_name', 'last_name', 'contact_phone', 'address', 'base', 'field']

    #redirecting upon update complete
    success_url = reverse_lazy('employees_app:creation_success')

    #THE POST METHOD IS CALLLED BEFORE THE FORM HAS BEEN SERVER-VALIDATED
    #adding a new value with the post method 
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        #code here 

        return super().post(request, *args, **kwargs)

    #using the form_valid method to add those new values
    def form_valid(self, form):
        employee = form.save()
        employee.full_name = employee.first_name + ' ' + employee.last_name
        employee.save()

        #syntax for returning the result  of the form valid
        return super(UpdateEmployee, self).form_valid(form)


#DeleteView section
class DeleteEmployee(DeleteView):
    template_name = 'employees/delete-employee.html'
    model = Employee

    success_url = success_url = reverse_lazy('employees_app:creation_success')


#TemplateView section
#creating a success view for the redirection with a simple template view
class CreationSuccess(TemplateView):
    template_name = "employees/success/creation-success.html"

#creating a success view for the redirection with a simple template view
class UpdateSuccess(TemplateView):
    template_name = "employees/success/update-success.html"

#creating a success view for the redirection with a simple template view
class DeletionSuccess(TemplateView):
    template_name = "employees/success/deletion-success.html"


