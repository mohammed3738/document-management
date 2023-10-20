from django import forms
from django.contrib.auth.forms import UserCreationForm  
from .models import *



class UserForm(UserCreationForm):
   

    class Meta:
        model = CustomUser
        fields = ['username', 'contact_number', 'email','password1','password2']