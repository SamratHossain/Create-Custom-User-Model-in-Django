from django.contrib.auth import get_user_model
from django import forms
from django.forms import fields
User = get_user_model()

class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password', 'phone', 'gender', 'dateofbirth']