from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        "class" : "form-control",
        "placeholder" : "email"
    }))
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        "class" : "form-control",
        "placeholder" : "firs_name"
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        "class" : "form-control",
        "placeholder" : "last_name"
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class" : "form-control",
        "placeholder" : "enter password"
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class" : "form-control",
        "placeholder" : "enter password again"
    }))

    class Meta:
        model = get_user_model()
        fields = ['email', 'first_name', 'last_name', 'password1', 'password2']

class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
            "class" : "form-control",
            "placeholder" : "email"
        })) 
    password     = forms.CharField(widget=forms.PasswordInput(attrs={
        "class" : "form-control",
        "placeholder" : "enter password"
    })) 

    