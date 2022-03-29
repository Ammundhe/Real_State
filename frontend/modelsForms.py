from django.forms import ModelForm, TextInput, EmailInput
from inquery.models import inquery


class inqueryForm(ModelForm):
    class Meta:
        model=inquery
        fields=["name", "email", "phoneNumber"]
        widgets = {
            'name':TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Name'
                }),
            'email': EmailInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'Email'
                }),
            'phoneNumber':TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Mobile Number'
                }),
        }