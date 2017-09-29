import threading
from amazon.api import AmazonAPI
from django.core.mail import send_mail
# from .settings import *
from ..models import *
from datetime import datetime


EMAIL_HOST_USER = 'trackamazonservice@gmail.com'


def update_product(product):
    url = product.product_url
    
    try:
        AMAZON_ACCESS_KEY = 'AKIAIZPHCO56EZACZHBA'
        AMAZON_SECRET_KEY = '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'
        AMAZON_ASSOC_TAG = '1015f-21'
        
        region = url.split("amazon.")[1].split("/")[0]
        
        if "/dp/" in url:
            ASIN = url.split("/dp/")[1].strip("/").split("/")[0]
        elif "/gp/" in url:
            ASIN = url.split("/gp/product/")[1].strip("/").split("/")[0]
        print(ASIN)
        
        amazon = AmazonAPI(AMAZON_ACCESS_KEY, AMAZON_SECRET_KEY, AMAZON_ASSOC_TAG, region=region.upper())
        products = amazon.lookup(ItemId=ASIN)
        price, currency = products.price_and_currency
        title = products.title
        graph = Graph(product_id=product, updated_at=datetime.now(), current_price=price)
        graph.save()
        
        product = Product.objects.get(asin=ASIN)
        user_products = User_products.objects.filter(product_id=product)
        
        for user_product in user_products:
            if user_product.price_drop_below:
                print(title, int(price),user_product.email_to)
                if int(price) <= int(user_product.price_drop_below):
                    print(user_product.user_id_id)
                    print("Price drop value = " + str(user_product.price_drop_below))
                    print("SENT MAILLLLL TOOOOOO " + str(user_product.email_to))
                    send_mail('Price dropped!', 'Hi, the price of ' + str(title) + "dropped from " + str(user_product.price_when_added) + " to " + str(price) + "\n\nFollow this link to buy now \n" + str(url), EMAIL_HOST_USER, [user_product.email_to], fail_silently=False)
        
    except Exception as e:
        print("ERROR " + str(e))
    return


def fetch_all_products():
    
    products = Product.objects.all()
    
    for product in products:
        update_product(product)

    # threading.Timer(5, update_product).start()


# if datetime.datetime.now().time().strftime('%H:%M:%S') == "12:00:00":
fetch_all_products()
