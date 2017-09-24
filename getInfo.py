# progressive web app chrome head tag

from amazon.api import AmazonAPI
# access key, secret key, associate tag
AMAZON_ACCESS_KEY = 'AKIAIZPHCO56EZACZHBA'
AMAZON_SECRET_KEY = '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'
AMAZON_ASSOC_TAG = '1015f-21'
url = "https://www.amazon.in/gp/product/B074H26CGL/"
img = "http://images.amazon.com/images/P/" + ASIN + ".01.jpg"
region = url.split("amazon.")[1].split("/")[0]
ASIN = url.split("/product/")[1].strip("/")
amazon = AmazonAPI(AMAZON_ACCESS_KEY, AMAZON_SECRET_KEY, AMAZON_ASSOC_TAG, region = region.upper())
products = amazon.lookup(ItemId=ASIN)
price, currency = products.price_and_currency
title = products.title
print(title)