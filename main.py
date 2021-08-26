import csv
import requests

from bs4 import BeautifulSoup

from utils import get_categories, get_jpg, books_of_category, get_product_info




# RETRIEVE ALL CATEGORIES
list_categories = get_categories()


#LISTE  IMAGES D UNE CATEGORIE (TRAVEL)
list_jpg_travel_categorie = get_jpg()


# RETURNS EVERY BOOKS OF CATEGORIES TRAVELD
list_title_categories_traveld = books_of_category('https://books.toscrape.com/catalogue/category/books/travel_2/index.html')



#RETOURNE PRODUCT INFO
#list_product_info = get_product_info('https://books.toscrape.com/catalogue/its-only-the-himalayas_981/index.html')
















