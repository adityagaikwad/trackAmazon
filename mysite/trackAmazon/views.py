# from django.http import HttpResponse
# from django.shortcuts import render
#
# from mysite.trackAmazon.controllers.forms import *
#
#
# def index(request):
#     if request.method == "POST":
#         # add product to product model and get full dictionary OR update the dict in "IF" part
#         form = UrlForm(request.POST)
#         url = ""
#         if form.is_valid():
#             di = get_products(url)
#             print("valid")
#             di = extract_params(url)
#             return render(request, "index.html", di)
#         return HttpResponse("invalid url")
#     else:
#         # get product details from product model and return that dict for our username
#         # get username from session
#         di_test = get_products()
#         url = "https://www.amazon.in/gp/product/B074H26CGL/"
#         ASIN = url.split("/product/")[1].strip("/")
#         img = "http://images.amazon.com/images/P/" + ASIN + ".01.jpg"
#         di = {"img_url": img}
#         form = UrlForm(request.POST, )
#         return render(request, "index.html", di)
#
# def get_products(url = None):
#     # if url is none then return dict corresponding to username stored in session
#     # if url not none then add new product and return new dict
#     return {}
#
# def login(request):
#     return render(request, "login.html")
#
# def register(request):
#     return render(request, "register.html")
#
# def contact(request):
#     return render(request, "contact.html")
#
#
# def extract_params(urls):
#     # get username from Models. uname = aditya for now
#     # product_urls = {'aditya': {'iphone': {'current_price': 0, 'decrease': 0, 'increase': 0}}}
#     product_urls = {}
#     username = "aditya"
#     product_title = "iphone"
#     current_price = 0
#     increase = 0
#     decrease = 0
#     url = "https://www.amazon.in/gp/product/B074H26CGL/"
#     ASIN = url.split("/product/")[1].strip("/")
#     img = "http://images.amazon.com/images/P/" + ASIN + ".01.jpg"
#
#     if username not in product_urls:
#         product_urls["username"] = username
#         product_urls[username] = {}
#         product_urls[username][product_title] = {"current_price": current_price, "increase": increase,
#                                                  "decrease": decrease, "img_url": img}
#     else:
#         product_urls["username"] = username
#         product_urls[username][product_title] = {"current_price": current_price, "increase": increase,
#                                                  "decrease": decrease, "img_url": img}
#     print(product_urls)
#
#     # Get asin from form url
#     ASIN = "https://www.amazon.in/gp/product/B074H26CGL/"
#     ASIN.split("/product/")[1].strip("/")
#     print(ASIN)
#     img = "http://images.amazon.com/images/P/" + ASIN + ".01.LZ.jpg"
#     return product_urls