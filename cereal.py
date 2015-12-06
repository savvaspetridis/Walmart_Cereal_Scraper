import MySQLdb
from string import digits
import requests
import datetime

class cereal():
	def __init__(self, brand, name, rate_num, rating, time, page, position, search_term):
		self.brand = brand
		self.name = name
		self.rateNum = rate_num
		self.rating = rating
		self.time = time
		self.page = page
		self.position = position
		self.search_term = search_term

db = MySQLdb.connect(host="localhost",
					 user="root",
					 db = "yum")

def get_brand(name):
	brand = 'Other'
	if "Kellog" in name:
		brand = "Kellogg's"
	if "Post" in name:
		brand = "Post"
	if "Cheerios" in name:
		brand = "Cheerios"
	if "Kashi" in name:
		brand = "Kashi"
	return brand

### SEARCH TERMS ###
search_1 = "cereal"
search_2 = "cold cereal"

time_of_test = datetime.datetime.now()

def scrape(search_term, page_num, time_of_test):

	payload = {'query': search_term, 'page': str(page_num)}
	req = requests.get('http://www.walmart.com/search/', params=payload)

	print (req.url)

	### Search "cereal" ###
	cereal_info = req.text.encode('utf-8')

	### LIST OF CEREALS -- 20 CEREALS PER PAGE ###
	buff_cereal_list = [0 for x in range(20)]

	blocks = cereal_info.split('data-item-id')

	del blocks[0]

	### FILL CEREAL LIST ###
	i = 0
	while (i < len(blocks)):

		print "Cereal #" + str(i + 1) + ":"

		new_cereal = cereal
	
		### GET CEREAL NAME ###
		cereal_block = blocks[i].split('img class=product-image alt')

		other_info = cereal_block[1]
	
		### GET NUMBER OF RATINGS // FORMAT NUMBER ###
		# Check if there are ratings
		num_of_ratings = "NONE"
		if 'stars-reviews' in other_info: 
			num_of_ratings = (((other_info.split('stars-reviews>'))[1]).split(' '))[0].replace('(', '').replace(')', '')

		### GET RATING // FORMAT RATING ###
		# Check if there is an average rating
		rating = "NONE"
		if 'class=visuallyhidden>' in other_info:
			rating = (((other_info.split('class=visuallyhidden>'))[1]).split(' '))[0]

		### FORMAT CEREAL NAME ###
		cereal_name = (cereal_block[0].split('ip/'))[1]
		cereal_name = (cereal_name.split('z/'))[0].replace('-', ' ').translate(None, digits)[:-3]

		print "Full Name: " + cereal_name
	
		cereal_brand = get_brand(cereal_name)

		print "Brand: " + cereal_brand
		print "Number of ratings: " + num_of_ratings
		print "Rating: " + rating
		print "\n"


		new_cereal = cereal(cereal_brand, cereal_name, num_of_ratings, rating, time_of_test, page_num, i, search_term)
	
		### INSERT NEW CEREAL OBJECT INTO BUFFER ###
		buff_cereal_list[i] = new_cereal

		i = i + 1 

	### PRINT CEREAL LIST ###

	'''
	i = 0
	while (i < len(cereal_list)):
		print str(i) + ": " + str(cereal_list[i])
		i = i + 1
	'''

	return buff_cereal_list


page_list = [1, 2, 3]

cereal_list = scrape(search_1, 3, time_of_test)

def scrape_and_insert(search_term, page_num, time_of_test, page_list):

	i = 0
	while (i < len(page_list)):
		page = page_list[i]
		cereal_list = scrape(search_term, page, time_of_test)
		insert(cereal_list)
		i = i + 1

def insert(cereal_list):

	i = 0
	while( i < len(cereal_list)): 
		cereal_i = cereal_list[i]
		i = i + 1







