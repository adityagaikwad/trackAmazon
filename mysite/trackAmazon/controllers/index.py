from django.http import HttpResponse
from django.shortcuts import render
from ..forms import *
from .logout import *
from .get_products import *
from django.conf import settings
from django.core.mail import send_mail
import decimal


def index_req(request):
    
    # add error field in render if length_old = new length "product already added"
    
    if request.method == "POST":
        if "save" in request.POST:
            print("TRYING TO ADD PRICE DROP VALUE")
            if "email" in request.session:
                # check for drop value when updating graph and send mail
                # remove mail from here
                # send_mail('hello', 'hi', settings.EMAIL_HOST_USER, ['gujarshlok@gmail.com'], fail_silently=False)
                
                # update price_drop in user_products
                user = Users.objects.filter(email=request.session["email"])
                if user.exists():
                    email_to = request.POST["alert_pref_email"]
                    print(email_to)
                    print(request.POST)
                    price_drop = request.POST["alert_price"]
                    print(price_drop)
                    title = request.POST["hidden-title"]
                    print(title)
                    # get title from AJAX
                    
                    # title = "Boat Rockerz 400 On-Ear Bluetooth Headphones (Carbon Black)"
                    product = Product.objects.filter(title=title)
                    if product.exists():
                        user_product = User_products.objects.get(user_id=user, product_id=product)
                        # print(user_product.id)
                        user_product.price_drop_below = price_drop
                        user_product.email_to = email_to
                        user_product.save()
                        print(user_product.price_drop_below)
                        print(user_product.email_to)
                        print("ADDED PRICE DROP VALUE")
                    
                    list_of_product_dicts = get_products(request)
                    form = UrlForm()
                    email_id = request.session['email']
                    username = request.session['username']
                    return render(request, "index.html",
                                  {"Login": "True", "username": username, "data": list_of_product_dicts, "form": form})

            return HttpResponse("Invalid call to modal")

        elif "url" in request.POST:
            email = request.session["email"]
            # add product to product model and get full dictionary OR update the dict in "IF" part
            print("IN INDEX FORM SUBMITTED")
            form = UrlForm(request.POST)
            print(email)
            print(form.data["url"])
            if form.is_valid():
                url = form.cleaned_data["url"]
                list_of_product_dicts = get_products(request, url)
                # print(url)
                form = UrlForm()
                print("URL VALID")
                username = request.session["username"]
                return render(request, "index.html",
                              {"Login": "True", "username": username, "data": list_of_product_dicts, "form": form})
            else:
                return HttpResponse("invalid url")
        
        elif "login" in request.POST:
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
                return render(request, "login.html", {"error": "email", 'data': zip(form, li)})
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
