from django.http import HttpResponse
from django.shortcuts import render
from ..api.get_products import *
from ..forms import *
from ..models import *


def register(request):
    if request.method == "POST":
            print("IN REGISTER FORM SUBMITTED")
            form = RegisterForm(request.POST)
            print(form.errors)
            if form.is_valid():
                email_id = form.cleaned_data['email']
                password = form.cleaned_data['password']
                username = form.cleaned_data['username']
                password2 = form.cleaned_data['password2']
                
                if password == password2:
                    form.save()
                    request.session['email'] = email_id
                    request.session['username'] = username
                    list_of_product_dicts = get_products(request)
                    form = UrlForm()
                    return render(request, "index.html",
                                      {"Login": "True", "username": username, "data": list_of_product_dicts,
                                       "form": form})
                
                # else, if passwords do not match
                else:
                    form = RegisterForm()
                    li = ["Username", "Email", "Password", "Confirm Password"]
                    return render(request, "register.html", {"error": "password", 'data': zip(form, li)})
                
            else:
                form = RegisterForm()
                li = ["Username", "Email", "Password", "Confirm Password"]
                return render(request, "register.html", {"error": "exists", 'data': zip(form, li)})
    else:
        form = RegisterForm()
        li = ["Username", "Email", "Password", "Confirm Password"]
        return render(request, "register.html", {'data': zip(form, li)})
