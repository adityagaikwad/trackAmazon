from django.shortcuts import render
from ..forms import *
from ..api.get_products import *
from django.contrib.auth.hashers import check_password


def login(request):
    if request.method=="POST":
        print("IN LOGIN FORM SUBMITTED")
        form = LoginForm(request.POST)
    
        if form.is_valid():
            email = form.cleaned_data['email']
            print(email)
            password = form.cleaned_data['password']
            try:
                user_obj = Users.objects.get(email=email)
            except:
                form = LoginForm()
                li = ["Email", "Password"]
                return render(request, "login.html", {"error": "register", 'data': zip(form, li)})
            
            if user_obj:
                username = user_obj.username
                if check_password(password, user_obj.password):
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
            return render(request, "login.html", {"error": "email", 'data': zip(form, li)})
    else:
        form = LoginForm()
        li = ["Email", "Password"]
        return render(request, "login.html", {'data': zip(form, li)})
