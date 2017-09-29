from django import forms
from .models import *
from django.contrib.auth.hashers import make_password


class UrlForm(forms.Form):
    url = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter product link like https://www.amazon.in/Apple-iPhone-5s-Gold-16GB/dp/B00FXLCD38'}))

    
class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Password'}))


class RegisterForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter username'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm password'}))
    class Meta:
        model = Users
        fields = ['username', 'email', 'password']

    def clean_password(self):
        password = self.cleaned_data['password']
        # crypt stuff
        hashed_pwd = make_password(password)
        return hashed_pwd
    