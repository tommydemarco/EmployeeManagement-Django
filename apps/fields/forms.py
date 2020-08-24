from django import forms

#importing the model
from .models import Field

#create the multimodel form
class NewFieldForm(forms.ModelForm):

    class Meta:
        model = Field
        #here fields go in a tuple and not in a list
        fields = ('field_name', 'alt_name')
        #adding form features with the widgets class variable
        widgets = {
            'field_name': forms.TextInput(
                attrs = {
                    'placeholder':'Insert the first name',
                    'class':'form-control'
                }
            ),
            'alt_name': forms.TextInput(
                attrs = {
                    'placeholder':'Insert the first name',
                    'class':'form-control'
                }
            ),           
        }