from django.http import HttpResponse
from django.shortcuts import render
from ..forms import *
from .check_validation import *


def index_req(request):
    # if not check_login(request):
    #     form = LoginForm()
    #     li = ["Email", "Password"]
    #     return render(request, "login.html", {"error": "password", 'data': zip(form, li)})
    
    if request.method == "POST":
        if "url" in request.POST:
            # add product to product model and get full dictionary OR update the dict in "IF" part
            print("IN INDEX FORM SUBMITTED")
            form = UrlForm(request.POST)
            url = ""
            if form.is_valid():
                di = get_products(url)
                print("valid")
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
                # print(user_obj.username)
                except:
                    form = LoginForm()
                    li = ["Email", "Password"]
                    return render(request, "login.html", {"error": "email", 'data': zip(form, li)})
                if user_obj:
                    username = user_obj.username
                    if user_obj.password == password:
                        # request.session['username'] = username
                        # request.session['logged_in'] = "True"
                        print(username)
                        return render(request, "index.html", {"Login": "True", "username": username})
                    else:
                        print("Password")
                        form = LoginForm()
                        li = ["Email", "Password"]
                        return render(request, "login.html", {"error": "password", 'data': zip(form, li)})
                else:
                    form = LoginForm()
                    li = ["Email", "Password"]
                    return render(request, "login.html", {"error": "register", 'data': zip(form, li)})
            else:
                form = LoginForm()
                print("BOTH")
                li = ["Email", "Password"]
                return render(request, "login.html", {"error": "both", 'data': zip(form, li)})
    else:
        # get product details from product model and return that dict for our username
        # get username from session
        di_test = get_products()
        url = "https://www.amazon.in/gp/product/B074H26CGL/"
        ASIN = url.split("/product/")[1].strip("/")
        img = "http://images.amazon.com/images/P/" + ASIN + ".01.jpg"
        di = {"img_url": img}
        form = UrlForm()
        return render(request, "index.html", di)

def get_products(url = None):
    # if url is none then return dict corresponding to username stored in session
    # if url not none then add new product and return new dict
    return {}
