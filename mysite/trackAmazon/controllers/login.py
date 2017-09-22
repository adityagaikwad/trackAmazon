from django.shortcuts import render
from .check_validation import *
from ..forms import *


def login(request):
    # if request.method == "POST":
    #     print("IN LOGIN FORM SUBMITTED")
    #     form = LoginForm(request.POST)
    #     if form.is_valid():
    #         email = form.cleaned_data['email']
    #         password = form.cleaned_data['password']
    #         try:
    #             user_obj = Users.objects.get(email=email)
    #         # print(user_obj.username)
    #         except:
    #             form = LoginForm()
    #             li = ["Email", "Password"]
    #             return render(request, "login.html", {"error": "email", 'data': zip(form, li)})
    #         if user_obj:
    #             username = user_obj.username
    #             if user_obj.password == password:
    #                 # request.session['username'] = username
    #                 # request.session['logged_in'] = "True"
    #                 print(username)
    #                 return render(request, "index.html", {"Login": "True", "username": username})
    #             else:
    #                 print("Password")
    #                 form = LoginForm()
    #                 li = ["Email", "Password"]
    #                 return render(request, "login.html", {"error": "password", 'data': zip(form, li)})
    #         else:
    #             form = LoginForm()
    #             li = ["Email", "Password"]
    #             return render(request, "login.html", {"error": "register", 'data': zip(form, li)})
    #
    #     else:
    #         form = LoginForm()
    #         print("BOTH")
    #         li = ["Email", "Password"]
    #         return render(request, "login.html", {"error": "both", 'data': zip(form, li)})
    #     print("a")
    # else:
    form = LoginForm()
    li = ["Email", "Password"]
    return render(request, "login.html", {'data': zip(form, li)})