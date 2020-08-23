from django.shortcuts import render

#import the list view 
from django.views.generic import ListView, DetailView, CreateView 

#importing the model that is required in the class views
from .models import Employee

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
    #inserting a field class variable is necessary for the usage of a CreateView
    #to insert all fields assign the value ('__all__') to the fields variable
    fields = ['first_name', 'last_name', 'contact_phone', 'address', 'base', 'field']

    #adding the url for when the process is complete.
    #required in a CreateView
    success_url = "."

    
