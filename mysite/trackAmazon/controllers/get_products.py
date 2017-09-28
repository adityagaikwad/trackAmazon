from amazon.api import AmazonAPI
from ..models import *
from datetime import datetime


def get_products(request, url=None):
    # if url is none then return dict corresponding to username stored in session
    # if url not none then add new product and return new dict
    email_id = ""
    if "email" in request.session:
        email_id = request.session["email"]
        # email_id = "adityagaikwad009@gmail.com"
        try:
            user = Users.objects.get(email=email_id)
            print(email_id)
            # url = "https://www.amazon.in/dp/B073B3HYXR"
        except:
            return None
        
        # access key, secret key, associate tag
        if url is not None:
            # check if ASIN already exists in products model
            # else add in products and user_products
            try:
                print(url)
                print("TRYING TO GET URL DATA")
                AMAZON_ACCESS_KEY = 'AKIAIZPHCO56EZACZHBA'
                AMAZON_SECRET_KEY = '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'
                AMAZON_ASSOC_TAG = '1015f-21'
                region = url.split("amazon.")[1].split("/")[0]
                print(region)
                if "/dp/" in url:
                    ASIN = url.split("/dp/")[1].strip("/").split("/")[0]
                elif "/gp/" in url:
                    ASIN = url.split("/gp/product/")[1].strip("/").split("/")[0]
                print(ASIN)
                amazon = AmazonAPI(AMAZON_ACCESS_KEY, AMAZON_SECRET_KEY, AMAZON_ASSOC_TAG, region=region.upper())
                products = amazon.lookup(ItemId=ASIN)
                img = products.large_image_url
                price, currency = products.price_and_currency
                title = products.title
                print(title)
                # check if product is in Products table
                product = Product.objects.filter(asin=ASIN)
                if product.exists():
                    user_prod_check = User_products.objects.filter(product_id=product, user_id=user)
                    
                    if not user_prod_check.exists():
                        user_prod = User_products(user_id=user, product_id=product[0], price_when_added=price,
                                                  created_at=datetime.now(), updated_at=datetime.now())
                        print("EXISTS IN PRODUCT NOT IN USER_PRODUCT")
                        user_prod.save()
                        
                        graph = Graph(product_id=product[0], updated_at=datetime.now(), current_price=price)
                        graph.save()
                        return get_old_list(request)
                    else:
                        return get_old_list(request)
                else:
                    print("Adding NEW PRODUCT")
                    
                    product_new = Product(product_url=url, title=title, asin=ASIN, img_url=img, created_at=datetime.now())
                    product_new.save()
                    
                    user_prod = User_products(user_id=user, product_id=product_new, price_when_added=price,
                                              created_at=datetime.now(), updated_at=datetime.now())
                    user_prod.save()
                    # print("HIHIHIHIIIIIHIHI" + str(product_new.product_id))
                    graph = Graph(product_id=product_new, updated_at=datetime.now(), current_price=price)
                    graph.save()
            except:
                print("ERROR IN FETCHING PRODUCT")
                return get_old_list(request)

        # add this product to products list
        #
        # # products has list of product_dicts
        # print("GETTING PRODUCTS")
        # user_products = User_products.objects.filter(user_id=user.user_id).values()[::1]
        # product_ids = []
        # for prod in user_products:
        #     product = Product.objects.filter(product_id=prod["product_id_id"])
        #     graph = Graph.objects.filter(product_id=prod["product_id_id"]).last()
        #     print(prod["product_id_id"])
        #     if graph and product.exists() and "title" not in prod:
        #         prod["title"] = product[0].title
        #         prod["curr_price"] = graph.current_price
        #         # print("CURRENT PRICCEEEEEE" + str(graph.current_price))
        #         prod["img_url"] = product[0].img_url
        #         prod["updated_at"] = graph.updated_at
        #         prod["product_url"] = product[0].product_url
        #         if (prod["curr_price"] < prod["price_when_added"]):
        #             prod["profit"] = prod["price_when_added"] - prod["curr_price"]
        #         else:
        #             prod["loss"] = prod["curr_price"] - prod["price_when_added"]
        #
        return get_old_list(request)
    return None


def get_old_list(request):
    email_id = request.session["email"]
    print("GETTING PRODUCTS")
    
    user = Users.objects.get(email=email_id)
    
    user_products = User_products.objects.filter(user_id=user.user_id).values()[::1]
    
    for prod in user_products:
        product = Product.objects.filter(product_id=prod["product_id_id"])
        graph = Graph.objects.filter(product_id=prod["product_id_id"]).last()
        # print(prod["product_id_id"])
        if graph and product.exists() and "title" not in prod:
            prod["title"] = product[0].title
            prod["curr_price"] = graph.current_price
            # print("CURRENT PRICCEEEEEE" + str(graph.current_price))
            prod["img_url"] = product[0].img_url
            prod["updated_at"] = graph.updated_at
            prod["product_url"] = product[0].product_url
            if (prod["curr_price"] < prod["price_when_added"]):
                prod["profit"] = prod["price_when_added"] - prod["curr_price"]
            else:
                prod["loss"] = prod["curr_price"] - prod["price_when_added"]

    return user_products
