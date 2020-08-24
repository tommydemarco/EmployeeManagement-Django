from django.shortcuts import render

#importing the form view
from django.views.generic.edit import FormView

#importing the necessary forms
from .forms import NewFieldForm

class NewFieldView(FormView):
    template_name = "fields/add-new-field.html"
    form_class = NewFieldForm

    #required success URL
    success_url = '.'

    #form valid method
    def form_valid(self, form):

        #syntax for returning the result  of the form valid
        return super(NewFieldView, self).form_valid(form)