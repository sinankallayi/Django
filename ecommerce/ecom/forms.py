from django import forms
from django.contrib.auth.models import User
from ecom.models import Student

class CustomerUserForm(forms.ModelForm):
    
    class Meta:
        model =User 
        fields = ["first_name","last_name","username","password"]
        widget={
            "password":forms.PasswordInput()
        }

class StudentForm(forms.ModelForm):
    
    class Meta:
        model =Student 
        fields = ["first_name","last_name","date_of_birth","email"]
        