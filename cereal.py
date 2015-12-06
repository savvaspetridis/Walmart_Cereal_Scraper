'''
cereal.py written by Savvas Petridis
December 7, 2015
'''

import MySQLdb
import peewee
from peewee import *
from string import digits
import requests
import datetime

db = MySQLDatabase('yum', user='root')

class Cereal(peewee.Model):
	brand = peewee.TextField()
	name = peewee.TextField()
	rate_num = peewee.IntegerField()
	rating = peewee.TextField()
	time = peewee.TextField()
	page = peewee.IntegerField()
	position = peewee.IntegerField()
	search_term = peewee.TextField()

	class Meta:
		database = db

# Cereal.create_table()

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

# search terms
search_1 = "cereal"
search_2 = "cold cereal"

time_of_test = datetime.datetime.now()

def scrape(search_term, page_num, time_of_test):

	payload = {'query': search_term, 'page': str(page_num)}
	req = requests.get('http://www.walmart.com/search/', params=payload)

	# search "cereal" 
	cereal_info = req.text.encode('utf-8')

	blocks = cereal_info.split('data-item-id')

	del blocks[0]

	i = 0
	while (i < len(blocks)):

		print "Cereal #" + str(i + 1) + ":"
	
		# get cereal info
		cereal_block = blocks[i].split('img class=product-image alt')

		other_info = cereal_block[1]
	
		# check number of ratings
		# first check if there are ratings
		num_of_ratings = 0
		if 'stars-reviews' in other_info: 
			num_of_ratings = int((((other_info.split('stars-reviews>'))[1]).split(' '))[0].replace('(', '').replace(')', ''))

		# get rating
		# check if there is an average rating
		rating = "NONE"
		if 'class=visuallyhidden>' in other_info:
			rating = (((other_info.split('class=visuallyhidden>'))[1]).split(' '))[0]

		# format cereal name
		cereal_name = (cereal_block[0].split('ip/'))[1]
		cereal_name = (cereal_name.split('z/'))[0].replace('-', ' ').translate(None, digits)[:-3]

		print "Full Name: " + cereal_name
	
		cereal_brand = get_brand(cereal_name)

		print "Brand: " + cereal_brand
		print "Number of ratings: " + str(num_of_ratings)
		print "Rating: " + rating
		print "\n"

		# new cereal object
		specific_cereal = Cereal(brand=cereal_brand, name=cereal_name, rate_num=num_of_ratings, rating=rating, time=time_of_test, page=page_num, position=i, search_term=search_term)

		# insert cereal object into database
		specific_cereal.save()

		i = i + 1 


# list of pages to scrape
page_list = [1, 2, 3]

def scrape_and_insert(search_term, time_of_test, page_list):

	i = 0
	while (i < len(page_list)):
		page = page_list[i]
		scrape(search_term, page, time_of_test)
		i = i + 1

scrape_and_insert(search_2, time_of_test, page_list)








