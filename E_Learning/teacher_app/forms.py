from django import forms 

class Teacher_login_form(forms.Form):
        username=forms.CharField(max_length=30)
        password = forms.CharField(max_length=32, widget=forms.PasswordInput)

