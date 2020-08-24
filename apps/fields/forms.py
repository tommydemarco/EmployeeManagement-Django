from django import forms


#create the multimodel form
class NewFieldForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    field_name = forms.CharField(max_length=50)
    alt_name = forms.CharField(max_length=50)

    widgets = {
            first_name : forms.TextInput(
                attrs = {
                    'placeholder':'Insert the first name of the employee',
                    'class':'form-control'
                }
            ),
            'last_name': forms.TextInput(
                attrs = {
                    'placeholder':'Insert the last name of the employee',
                    'class':'form-control'
                }
            ),
            'field_name': forms.TextInput(
                attrs = {
                    'placeholder':'Insert the name of the field',
                    'class':'form-control'
                }
            ),
            'alt_name': forms.TextInput(
                attrs = {
                    'placeholder':'Insert the short name of the field',
                    'class':'form-control'
                }
            ),

        }