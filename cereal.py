from string import digits
import requests

class cereal():
	def __init__(self, brand, name, rate_num, rating):
		self.brand = brand
		self.name = name
		self.rateNum = rateNum
		self.rating = rating

def get_brand(name):
	brand = 'NONE'
	if "Kellog" in name:
		brand = "Kellogg's"
	if "Post" in name:
		brand = "Post"
	if "Cheerios" in name:
		brand = "Cheerios"
	if "Kashi" in name:
		brand = "Kashi"
	return brand

### BRANDS ### 
brand_che = "Cheerios"
brand_kas = "Kashi"
brand_kel = "Kellogg's"
brand_pos = "Post"


### SEARCH TERMS ###
search_1 = "cereal"
search_2 = "cold cereal"

page_num = 3

payload = {'query': search_1, 'page': str(page_num)}
req = requests.get('http://www.walmart.com/search/', params=payload)

print (req.url)


### Search "cereal" ###
cereal_info = req.text.encode('utf-8')

### LIST OF CEREALS ###
cereal_list = [0 for x in range(20)]

blocks = cereal_info.split('data-item-id')

del blocks[0]


### FILL CEREAL LIST ###
i = 0
while (i < len(blocks)):

	print "Cereal #" + str(i) + ":"

	new_cereal = cereal
	
	### GET CEREAL NAME ###
	cereal_block = blocks[i].split('img class=product-image alt')

	other_info = cereal_block[1]
	
	### GET NUMBER OF RATINGS // FORMAT NUMBER ###
	num_of_ratings = (((other_info.split('stars-reviews>'))[1]).split(' '))[0].replace('(', '').replace(')', '')

	print "Rating Total: " + num_of_ratings

	### GET RATING // FORMAT RATING ###
	rating = (((other_info.split('class=visuallyhidden>'))[1]).split(' '))[0]

	print "Rate: " + rating

	### FORMAT CEREAL NAME ###
	cereal_name = (cereal_block[0].split('ip/'))[1]
	cereal_name = (cereal_name.split('z/'))[0].replace('-', ' ').translate(None, digits)[:-3]

	print "Full Name: " + cereal_name
	
	cereal_brand = get_brand(cereal_name)

	print "Brand: " + cereal_brand


	# new_cereal = cereal
	
	### INSERT NAME INTO CEREAL LIST ###
	cereal_list[i] = cereal_name

	i = i + 1 

### PRINT CEREAL LIST ###

'''
i = 0
while (i < len(cereal_list)):
	print str(i) + ": " + str(cereal_list[i])
	i = i + 1
'''



# Search "cold cereal"
req_2 = requests.get('http://www.walmart.com/search/?query=' + search_2)
cold_info = req_2.text




