from amazon.api import AmazonAPI
from ..models import *
from datetime import datetime

def get_products(url=None, email_id = None):
    # if url is none then return dict corresponding to username stored in session
    # if url not none then add new product and return new dict
    email_id = "adityagaikwad009@gmail.com"
    user_id = Users.objects.get(email=email_id).user_id
    print(user_id)
    
    # access key, secret key, associate tag
    if url is not None:
        # check if ASIN already exists in products model
        # else add in products and user_products
        AMAZON_ACCESS_KEY = 'AKIAIZPHCO56EZACZHBA'
        AMAZON_SECRET_KEY = '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'
        AMAZON_ASSOC_TAG = '1015f-21'
        url = "https://www.amazon.in/gp/product/B074H26CGL/"
        region = url.split("amazon.")[1].split("/")[0]
        ASIN = url.split("/product/")[1].strip("/")
        img = "http://images.amazon.com/images/P/" + ASIN + ".01.jpg"
        amazon = AmazonAPI(AMAZON_ACCESS_KEY, AMAZON_SECRET_KEY, AMAZON_ASSOC_TAG, region=region.upper())
        products = amazon.lookup(ItemId=ASIN)
        price, currency = products.price_and_currency
        title = products.title
        print(title)
        ASIN = "ABCDEG"
        # check if product is in Products table
        product = Product.objects.filter(asin = ASIN)
        if product.exists():
            # change 2 for AutoField
            user_prod = User_products(2,user_id,product[0].product_id,price,datetime.now(), datetime.now())
            print("EXISTS")
            user_prod.save()
            
            graph = Graph(product[0].product_id,datetime.now(), price)
            graph.save()
            # print(graph)
        else:
            print("Adding NEW PRODUCT")
            # CHANGE HARDCODED AUTOFIELDS
            
            product_new = Product(3,url,title,ASIN,img,datetime.now())
            product_new.save()
            
            user_prod = User_products(3,user_id, product_new.product_id, price, datetime.now(),datetime.now())
            user_prod.save()
            
            graph = Graph(1,product_new.product_id, datetime.now(), price)
            graph.save()

    #   add this product to products list
    
    # products has list of product_dicts
    
    products = User_products.objects.filter(user_id=user_id).values()[::1]
    # for product in products:
    #     print(product['created_at'])
    
    # insert
    # into
    # 'trackAmazon_user_products'('id', 'price_when_added', 'product_id', 'user_id', 'created_at', 'updated_at')
    # values(1, 1, 1, 1, '1-1-12', '1-1-12')
    
    return (products)
