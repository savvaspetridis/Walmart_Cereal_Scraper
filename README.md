# Walmart_Cereal_Scraper

This is a neat little program that scrapes some cereal info from Walmart's website. 

Dependencies:
pip install requests
pip install peewee

Primary file: cereal.py

This script takes some data regarding four cereal brands sold by Walmart and inserts it into a MYSQL database. 

~~ In order to run this script in its full effect: 

1. You will need to create a MYSQL database and replace the relevant fields on this line: 

db = MySQLDatabase(.....)

2. Uncomment this line: Cereal.create_table()

3. Run the script: # python cereal.py

~~ How to modify the script to collect certain data:  

The function 'scrape_and_insert' calls the 'scrape' function and takes in three fields: search_term, time_of_test, and page_list

search_term is the term to be searched, like "cereal" or "cold cereal"
time_of_test is the time the program is being run
page_list is a list of pages to collect data from like: [1, 2, 3] or [1, 2, 3, 4, 5, 6] 

scrape_and_insert is called at the very end of the file. Modify these three parameters to customize your run!

Thanks for checking this out!









 
