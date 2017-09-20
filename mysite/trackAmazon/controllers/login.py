from django.http import HttpResponse
from django.shortcuts import render
from .forms import *


def login(request):
    if request.method == "POST":
        print("IN LOGIN FORM SUBMITTED")
        form = LoginForm(request.POST)
        if form.is_valid():
            return HttpResponse("Valid")
        else:
            return HttpResponse("Invalid")
    else:
        form = LoginForm()
        li = ["Username", "Email", "Password"]
        return render(request, "login.html", {'data': zip(form, li)})