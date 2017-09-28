import threading
from amazon.api import AmazonAPI
from ..models import *
from datetime import datetime


def update_product(product):
    url = product.product_url
    
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
    
    graph = Graph(product_id=product, updated_at=datetime.now(), current_price=price)
    graph.save()
    return


def fetch_all_products():
    
    products = Product.objects.all()
    
    for product in products:
        update_product(product)

    # threading.Timer(5, update_product).start()


# if datetime.datetime.now().time().strftime('%H:%M:%S') == "12:00:00":
fetch_all_products()
