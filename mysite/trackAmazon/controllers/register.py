from django.shortcuts import render

from ..forms import *


def register(request):
    # if request.method == "POST":
    #                # return render(request, "register.html", {"form": form})
    # else:
    form = RegisterForm()
    li = ["Username", "Email", "Password", "Confirm Password"]
    return render(request, "register.html", {'data': zip(form, li)})
