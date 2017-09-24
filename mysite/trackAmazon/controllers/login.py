from django.shortcuts import render
from ..forms import *


def login(request):
    form = LoginForm()
    li = ["Email", "Password"]
    return render(request, "login.html", {'data': zip(form, li)})