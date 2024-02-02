from django import forms 
from administrator.models import Administrative_Data

class admintrator_login_form(forms.Form):
        username=forms.CharField(max_length=10)
        password = forms.CharField(max_length=32, widget=forms.PasswordInput)

