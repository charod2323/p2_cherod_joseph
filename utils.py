import csv

import requests

from bs4 import BeautifulSoup


url = 'https://books.toscrape.com/catalogue/category/books/travel_2/index.html'
page = requests.get(url)
soup = BeautifulSoup(page.content,'html.parser')

#RETURNS EVERY CATEGORIES OF BOOKSCRAP
def get_categories():

    f =  soup.find('aside',{'class':'sidebar col-sm-4 col-md-3'}).find('ul').findAll('li')

    listCategorie = []
    for i in range (1,51):
        a = f[i].text.replace("\n","")
        b = a.strip()
        listCategorie.append(b)
    print("\n".join(listCategorie))
    print("")
    print("")
    

#LISTE  IMAGES D UNE CATEGORIE (TRAVEL) 


def get_jpg():
    
    images = soup.findAll('div',{'class':'image_container'})

    img_list = []  
    for i in images:
        t = i.find('img')
        w = t['src']
        h = w.replace('../../../../','https://books.toscrape.com/')
        img_list.append(h)
    print("\n".join(img_list)) 
    print("")
    print("")


# RETURNS EVERY BOOKS OF CATEGORIES TRAVELD

def books_of_category(category_title):
    
     url = category_title  
     titre_categorie_traveld = soup.findAll('h3') 
     for t in titre_categorie_traveld:
         w = t.find('a')
         z = w['title']
         print(z)
     print("")
     print("")

"""

#RETOURNE PRODUCT INFO D'UN LIVRES D'UNE CATEGORIE (TRAVELD)


def get_product_info(products_info):

url = 'https://books.toscrape.com/catalogue/its-only-the-himalayas_981/index.html'
page = requests.get(url)
soup = BeautifulSoup(page.content,'html.parser')
categorie = soup.find('ul',{'class':'breadcrumb'}).findAll('li') 
product_info_key = soup.find('table',{'class':'table table-striped'}).findAll('th')
product_info_value = soup.find('table',{'class':'table table-striped'}).findAll('td')
title = soup.find('div',{'class':'col-sm-6 product-main'}).find('h1')
print(title)



product_info = {
                       "title": title.text,
                       "category": categorie[2].text,                       
                       product_info_key[0].text: product_info_value[0].text,
                       product_info_key[1].text: product_info_value[1].text,
                       product_info_key[2].text: product_info_value[2].text,
                       product_info_key[3].text: product_info_value[3].text,
                       product_info_key[4].text: product_info_value[4].text,
                       product_info_key[5].text: product_info_value[5].text,
                       product_info_key[6].text: product_info_value[6].text
                    }

print("")
print("")
print(product_info) 
"""     