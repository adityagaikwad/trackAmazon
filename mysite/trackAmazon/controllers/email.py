from django.shortcuts import render
from ..forms import *


def email(request):
    form = EmailForm()
    li = ["email_id", "price"]
    return render(request, "login.html", {'data': zip(form, li)})