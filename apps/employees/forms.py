from django import forms

#importing the model
from .models import Employee


#create employee form
class CreateEmployee(forms.ModelForm):
    
    class Meta:
        model = Employee
        #here fields go in a tuple and not in a list
        fields = ('first_name', 'last_name', 'contact_phone', 'address', 'base', 'field')
        #adding form features with the widgets class variable
        widgets = {
            'first_name': forms.TextInput(
                attrs = {
                    'placeholder':'Insert the first name',
                    'class':'form-control'
                }
            ),
            'last_name': forms.TextInput(
                attrs = {
                    'placeholder':'Insert the first name',
                    'class':'form-control'
                }
            ),
            'contact_phone': forms.NumberInput(
                attrs = {
                    'placeholder':'Insert the phone number',
                    'class':'form-control'
                }
            ),
            'address': forms.TextInput(
                attrs = {
                    'placeholder':'Insert the employee\'s address',
                    'class':'form-control'
                }
            ),
            'base': forms.Select(
                attrs = {
                    'class':'form-control'
                }
            ),
            'field': forms.Select(
                attrs = {
                    'class':'form-control'
                }
            ),
            
        }

    #very powerful custom validation process
    #syntax: clean_field_name, can only validate one value at the time
    def clean_first_name(self):
        #getting the value first_name from the cleaned data
        first_name = self.cleaned_data['first_name']
        if first_name == "Default":
            raise forms.ValidationError("The default value is not accepted as a name")

        return first_name
