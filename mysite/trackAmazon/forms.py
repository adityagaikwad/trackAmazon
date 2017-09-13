from django import forms

class UrlForm(forms.Form):
    url = forms.CharField()