import csv

import requests

from bs4 import BeautifulSoup

url = 'https://books.toscrape.com/catalogue/category/books/travel_2/index.html'
page = requests.get(url)
soup = BeautifulSoup(page.content,'html.parser')


def get_categories():
    """
    Returns a list of every categories of bookscrap website.
    """
    f =  soup.find('aside',{'class':'sidebar col-sm-4 col-md-3'}).find('ul').findAll('li')
    categories = []
    for i in range(1, len(f)):
        a = f[i].text.replace("\n","")
        b = a.strip()
        categories.append(b)
    return categories
    

def get_jpg():
    """
    Return a list of jpg category (travel).
    """
    images = soup.findAll('div',{'class':'image_container'})

    img_list = []  
    for i in images:
        t = i.find('img')
        w = t['src']
        h = w.replace('../../../../','https://books.toscrape.com/')
        img_list.append(h)
    print("\n".join(img_list)) 


# RETURNS EVERY TITLES OF CATEGORIES TRAVELD
def books_of_category(category_url):
    
     url = category_url
     titre_categorie_traveld = soup.findAll('h3') 
     for t in titre_categorie_traveld:
         w = t.find('a')
         z = w['title']
         print(z)
     print("")
     print("")
     print("")
     print("")


#RETURN PRODUCT INFO D'UN LIVRES D'UNE CATEGORIE (TRAVELD)
def get_product_info(category_info ):
    
    url1 = category_info
    page1 = requests.get(url1)
    soup1 = BeautifulSoup(page1.content,'html.parser')
           
    title = soup1.find('h1')
    categorie = soup1.find('ul',{'class':'breadcrumb'}).findAll('li') 
    rating = soup1.find("div",{'class':'col-sm-6 product_main'})
    ratings = str(rating)[229:234].replace('"','') + "/five"
    product_info_keys = soup1.find('table',{"class":"table table-striped"}).findAll('tr')
    product_info_values = soup1.find('table',{"class":"table table-striped"}).findAll('tr')

    list_keys = [] 
    list_values = []    
    
    for product_info_key in product_info_keys:
        k = product_info_key.find('th')
        list_keys.append(k.text)    
    
    for product_info_value in product_info_values:
        v = product_info_value.find('td')
        list_values.append(v.text) 

    
    product_info = {
                       "title": title.text,
                       "category": categorie[2].text.replace("\n"," "),  
                       "rating" : ratings, 
                       list_keys[0]: list_values[0],                
                       list_keys[1]: list_values[1],
                       list_keys[2]: list_values[2],
                       list_keys[3]: list_values[3],
                       list_keys[4]: list_values[4],
                       list_keys[5]: list_values[5],
                       list_keys[6]: list_values[6]
                    }

    print("")
    print("")
    print(product_info) 


  

"""

header = ['product_info_key','product_info_value']
with open('case.csv','w') as list_file:
    writer = csv.writer(list_file, delimiter = ',')
    writer.writerow(header)
    for product_info_key, product_info_value in zip(list_keys, list_values):
        writer.writerow([product_info_key,product_info_value])
        
"""


def get_books_links_one_categorie(): 
    lienProductInfo = []

    liens = soup.findAll('div',{'class':'image_container'})
    for i in liens:
        a = i.find('a')
        link = a['href']
        lienProductInfo.append(link.replace('../../../','https://books.toscrape.com/catalogue/'))
    print("\n".join(lienProductInfo))    


def get_images_titles_urls_product_info_of_one_categorie(): 

    for x in range(10):

      lienProductInfo = []

      liens = soup.findAll('div',{'class':'image_container'})
      for i in liens:
            a = i.find('a')
            link = a['href']
            lienProductInfo.append(link.replace('../../../','https://books.toscrape.com/catalogue/'))

      url6 = lienProductInfo[x]  
      page6 = requests.get(url6)
      soup6 = BeautifulSoup(page6.content,'html.parser')

  
      titleBook = soup6.find('ul',{'class':'breadcrumb'}).find('li',{'class':'active'}) 

      images = soup6.find('div',{'class':'carousel-inner'}).find('div',{'class':'item active'})
      t = images.find('img')
      w = t['src']

  
      print("")
      print("") 
      print("images: ",w.replace('../../','https://books.toscrape.com/'))#images
      print("")
      print("")  
      print("titres: ",titleBook.string)#titres
      print("")
      print("")  
      print("url pages: ",lienProductInfo[x])#url de la page du livre
      print("")
      print("") 


      print("")
      print("")
      print("")
      print("")
      print("")
      print("") 


    for y in range(10):  

      url6 = lienProductInfo[y]  
      page6 = requests.get(url6)
      soup6 = BeautifulSoup(page6.content,'html.parser')      
  
      books = soup6.find('ul',{'class':'breadcrumb'}).findAll('li') 
      product = soup6.findAll('th')
      product2 = soup6.findAll('td')
      title = soup6.find('h1')

      product_info = {
                       "title": title.text,                                             
                       product[0].text: product2[0].text,
                       product[1].text: product2[1].text,
                       product[2].text: product2[2].text,
                       product[3].text: product2[3].text,
                       product[4].text: product2[4].text,
                       product[5].text: product2[5].text,
                       product[6].text: product2[6].text
                     }

      print("")
      print("")
      print(product_info) 


def get_url_category():
            
  # LIST: ADRESS URL OF EACH CATEGORY 
    f =  soup.find('aside',{'class':'sidebar col-sm-4 col-md-3'}).find('ul').findAll('li')

    listUrlCategorie = []
    j = 0

    for i in range (2,51):
        j = j + 1
        a = f[j].text.replace("\n","")
        b = a.strip()
        url1 = "https://books.toscrape.com/catalogue/category/books/"+str(b)+"_"+str(i)+"/index.html"
        page1 = requests.get(url1)
        soup1 = BeautifulSoup(page1.content,'html.parser')
        listUrlCategorie.append(url1)
        print(*listUrlCategorie,sep="\n")
