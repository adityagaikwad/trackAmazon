from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from .forms import *

def index_req(request):
    if request.method == "POST":
        # add product to product model and get full dictionary OR update the dict in "IF" part
        form = UrlForm(request.POST)
        url = ""
        if form.is_valid():
            di = get_products(url)
            print("valid")
            di = {}
            return render(request, "index.html", di)
        return HttpResponse("invalid url")
    else:
        # get product details from product model and return that dict for our username
        # get username from session
        di_test = get_products()
        url = "https://www.amazon.in/gp/product/B074H26CGL/"
        ASIN = url.split("/product/")[1].strip("/")
        img = "http://images.amazon.com/images/P/" + ASIN + ".01.jpg"
        di = {"img_url": img}
        form = UrlForm(request.POST, )
        return render(request, "index.html", di)

def get_products(url = None):
    # if url is none then return dict corresponding to username stored in session
    # if url not none then add new product and return new dict
    return {}
