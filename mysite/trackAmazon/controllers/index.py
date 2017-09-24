from django.http import HttpResponse
from django.shortcuts import render
from ..forms import *
from .get_products import *

def index_req(request):
    email_id = ""
    if request.method == "POST":
        if "url" in request.POST:
            # add product to product model and get full dictionary OR update the dict in "IF" part
            print("IN INDEX FORM SUBMITTED")
            form = UrlForm(request.POST)
            print(form.data['url_val'])
            if form.is_valid():
                url = form.cleaned_data['url_val']
                li = get_products(url, email_id)
                print(url)
                di = {}
                return render(request, "index.html", di)
            return HttpResponse("invalid url")
        elif "login" in request.POST:
            print("IN LOGIN FORM SUBMITTED")
            form = LoginForm(request.POST)
            if form.is_valid():
                email = form.cleaned_data['email']
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
                        return render(request, "index.html", {"Login": "True", "username": username})
                    else:
                        print("Password")
                        form = LoginForm()
                        li = ["Email", "Password"]
                        return render(request, "login.html", {"error": "password", 'data': zip(form, li)})
            else:
                form = LoginForm()
                li = ["Email", "Password"]
                return render(request, "login.html", {"error": "both", 'data': zip(form, li)})
        else:
            form = LoginForm()
            print("BOTH")
            li = ["Email", "Password"]
            return render(request, "login.html", {"error": "both", 'data': zip(form, li)})

    else:
        list_of_product_dicts = get_products()
        form = UrlForm()
        return render(request, "index.html", {"data": list_of_product_dicts})