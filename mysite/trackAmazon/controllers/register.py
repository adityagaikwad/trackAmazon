from django.http import HttpResponse
from django.shortcuts import render
from .forms import *

def register(request):
    if request.method == "POST":
        print("IN REGISTER FORM SUBMITTED")
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "index.html", {"Login": "True", "Text": "Logout"})
        else:
            return HttpResponse("Invalid")
            # return render(request, "register.html", {"form": form})
    else:
        form = RegisterForm()
        li = ["Username", "Email", "Password", "Confirm Password"]
        return render(request, "register.html", {'data': zip(form, li)})