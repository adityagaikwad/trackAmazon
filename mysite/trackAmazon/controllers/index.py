from django.http import HttpResponse
from django.shortcuts import render
from ..forms import *
from .logout import *
from .get_products import *
from django.conf import settings
from django.core.mail import send_mail


def index_req(request):
    if request.method == "POST":
        if "url" in request.POST:
            email = request.session["email"]
            # add product to product model and get full dictionary OR update the dict in "IF" part
            print("IN INDEX FORM SUBMITTED")
            form = UrlForm(request.POST)
            print(email)
            print(form.data["url"])
            if form.is_valid():
                url = form.cleaned_data["url"]
                list_of_product_dicts = get_products(request, url)
                print(url)
                form = UrlForm()
                print("URL VALID")
                username = request.session["username"]
                return render(request, "index.html",
                              {"Login": "True", "username": username, "data": list_of_product_dicts, "form": form})
            else:
                return HttpResponse("invalid url")
        elif "save" in request.POST:
            form = EmailForm(request.POST)
            email = request.session["email_id"]
            print(email)
            if form.is_valid():
                email_id = form.cleaned_data["email_id"]
                price = form.cleaned_data["price"]

                return render(request,"index.html")
            else:
                return HttpResponse("invalid")

        elif "login" in request.POST:
            print("IN LOGIN FORM SUBMITTED")
            form = LoginForm(request.POST)
            send_mail('hello', 'hi', settings.EMAIL_HOST_USER, ['gujarshlok@gmail.com'], fail_silently=False)
            if form.is_valid():
                email = form.cleaned_data['email']
                print(email)
                password = form.cleaned_data['password']
                try:
                    user_obj = Users.objects.get(email=email)
                except:
                    form = LoginForm()
                    li = ["Email", "Password"]
                    return render(request, "login.html", {"error": "email", 'data': zip(form, li)})
                if user_obj:
                    username = user_obj.username
                    if user_obj.password == password:
                        print(username)
                        email_id = user_obj.email
                        form = UrlForm()
                        print("PROPER LOADING")
                        request.session['email'] = email_id
                        request.session['username'] = username
                        list_of_product_dicts = get_products(request)
                        return render(request, "index.html",
                                      {"Login": "True", "username": username, "data": list_of_product_dicts,
                                       "form": form})
                    else:
                        print("Password")
                        form = LoginForm()
                        li = ["Email", "Password"]
                        return render(request, "login.html", {"error": "password", 'data': zip(form, li)})
            else:
                form = LoginForm()
                li = ["Email", "Password"]
                return render(request, "login.html", {"error": "both", 'data': zip(form, li)})
        elif "register" in request.POST:
            print("IN REGISTER FORM SUBMITTED")
            form = RegisterForm(request.POST)
            print(form.errors)
            if form.is_valid():
                form.save()
                email_id = form.cleaned_data['email']
                password = form.cleaned_data['password']
                username = form.cleaned_data['username']
                request.session['email'] = email_id
                request.session['username'] = username
                list_of_product_dicts = get_products(request)
                form = UrlForm()
                return render(request, "index.html",
                              {"Login": "True", "username": username, "data": list_of_product_dicts,
                               "form": form})
            else:
                return HttpResponse("Invalid Register form")
        else:
            form = LoginForm()
            print("BOTH")
            li = ["Email", "Password"]
            return render(request, "login.html", {"error": "both", 'data': zip(form, li)})
    
    else:
        if "email" not in request.session:
            list_of_product_dicts = get_products(request)
            form = UrlForm()
            # print(form)
            print("REFRESH CALLED")
            return render(request, "index.html", {"data": list_of_product_dicts, "form": form})
        else:
            email_id = request.session['email']
            username = request.session['username']
            list_of_product_dicts = get_products(request)
            form = UrlForm()
            return render(request, "index.html",
                          {"Login": "True", "username": username, "data": list_of_product_dicts, "form": form})
