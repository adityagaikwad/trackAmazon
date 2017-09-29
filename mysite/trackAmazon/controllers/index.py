from django.http import HttpResponse
from django.shortcuts import render
from ..forms import *
from ..api.get_products import *


def index_req(request):
    
    if request.method == "POST":
        
        if "save" in request.POST:
            print("TRYING TO ADD PRICE DROP VALUE")
            if "email" in request.session:
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
        
    else:
        if "email" not in request.session:
            print("NOT LOGGED IN, IN INDEX PAGE")
            return render(request, "index.html")
        else:
            email_id = request.session['email']
            username = request.session['username']
            list_of_product_dicts = get_products(request)
            form = UrlForm()
            return render(request, "index.html",
                          {"Login": "True", "username": username, "data": list_of_product_dicts, "form": form})
