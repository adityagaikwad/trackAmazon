# progressive web app chrome head tag

from amazon.api import AmazonAPI
# access key, secret key, associate tag
AMAZON_ACCESS_KEY = 'AKIAIZPHCO56EZACZHBA'
AMAZON_SECRET_KEY = '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'
AMAZON_ASSOC_TAG = '1015f-21' 
amazon = AmazonAPI(AMAZON_ACCESS_KEY, AMAZON_SECRET_KEY, AMAZON_ASSOC_TAG, region = "IN")
products = amazon.lookup(ItemId='B00FREQBXE')
a = products.price_and_currency
if a:
	print(a)
