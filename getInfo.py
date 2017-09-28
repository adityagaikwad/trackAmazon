# progressive web app chrome head tag

from amazon.api import AmazonAPI
# access key, secret key, associate tag
AMAZON_ACCESS_KEY = 'AKIAIZPHCO56EZACZHBA'
AMAZON_SECRET_KEY = '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'
AMAZON_ASSOC_TAG = '1015f-21'
url = "https://www.amazon.in/Boat-Rockerz-400-Bluetooth-Headphones/dp/B01J82IYLW/"
region = url.split("amazon.")[1].split("/")[0]
ASIN = "B01M9C51T9"
amazon = AmazonAPI(AMAZON_ACCESS_KEY, AMAZON_SECRET_KEY, AMAZON_ASSOC_TAG, region = region.upper())
products = amazon.lookup(ItemId=ASIN)
price, currency = products.price_and_currency
print(price)
print(products.title)
title = products.title
print(products.large_image_url)