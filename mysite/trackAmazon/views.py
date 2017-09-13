from django.shortcuts import render, render_to_response
from .forms import *

def index(request):
    li = []
    if request.method == "POST":
        form = UrlForm(request.POST)
        if form.is_valid():
            print("valid")
            form.save()
            li.append("h")
        print(li)
        res = {'response': "Added"}
        return render(request, "login.html", res)
    else:
        form = UrlForm(data=request.POST)
        return render(request, "index.html", {'form': form})

def login(request):
    return render(request, "login.html")

def register(request):
    return render(request, "register.html")

def contact(request):
    return render(request, "contact.html")