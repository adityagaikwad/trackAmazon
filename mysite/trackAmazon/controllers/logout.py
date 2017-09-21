from django.http import HttpResponse
from django.shortcuts import render
from ..forms import *
from .check_validation import *


def logout(request):
    try:
        check_login(request)
        del request.session['username']
    except:
        pass
    form = LoginForm()
    print("IN LOGOUT")
    li = ["Email", "Password"]
    return render(request, "login.html", {'data': zip(form, li)})