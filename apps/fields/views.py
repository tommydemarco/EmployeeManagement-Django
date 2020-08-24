from django.shortcuts import render

#importing the form view
from django.views.generic import CreateView

#importing the necessary forms
from .forms import NewFieldForm

#importing messages 
from django.contrib import messages

#importing reverse lazy
from django.urls import reverse_lazy

class NewFieldView(CreateView):
    template_name = "fields/add-new-field.html"
    form_class = NewFieldForm

    #required success URL
    success_url = reverse_lazy('employees_app:add_new_employee')

    #form valid method
    def form_valid(self, form):

        success_message = messages.add_message(self.request, messages.SUCCESS, 
        'The new field was added to the database. You can now add an emmployee for the new field.')
        #syntax for returning the result  of the form valid
        return super(NewFieldView, self).form_valid(form)