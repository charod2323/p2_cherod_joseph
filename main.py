
from utils1 import  get_url_category, get_books_links_one_categorie, get_products




#GET ADRESS URL OF PAGES EACH CATEGORY
adress_category = get_url_category() 
#print(list_adress_category)   

#GET ALL LINKS BOOKS ONE CATEGORIE (TRAVELD)
books_links = get_books_links_one_categorie(adress_category)

#GET PRODUCT INFO ALL BOOKS ONE CATEGORIE
infos_books = get_products(books_links)