from django import forms 

class admintrator_login_form(forms.Form):
        username=forms.CharField(max_length=20)
        password = forms.CharField(max_length=32, widget=forms.PasswordInput)

