from bs4 import BeautifulSoup
import csv
import requests



"""
Choisissez n'importe quelle page Produit sur le site de Books to Scrape. Écrivez un script Python qui visite cette page et en extrait les informations suivantes :

product_page_url
universal_ product_code (upc)
title
price_including_tax
price_excluding_tax
number_available
product_description
category
review_rating
image_url

Écrivez les données dans un fichier CSV qui utilise les champs ci-dessus comme en-têtes de colonnes.
"""


def get_product_info(category_info ):
  
#Return product info of one book
      
  url1 = category_info
  page1 = requests.get(url1)
  soup1 = BeautifulSoup(page1.content,'html.parser')

  product_info = []
           
  title = soup1.find('h1')
  categorie = soup1.find('ul',{'class':'breadcrumb'}).findAll('li')
  category = categorie[2].text.replace("\n"," ")
  ratings = soup1.findAll('p')
  review_rating = ratings[2]['class'] 
  product_info_keys = soup1.find('table',{"class":"table table-striped"}).findAll('tr')
  product_info_values = soup1.find('table',{"class":"table table-striped"}).findAll('tr')
  images = soup1.findAll('div',{'class':'item active'})
  
  for i in images:
        t = i.find('img')
        w = t['src']
        image_url = w.replace('../../','https://books.toscrape.com/')


  list_keys = ["title","category","review_rating","image_url"] 
  list_values = [title.text,category,review_rating,image_url]  
      
  for product_info_key in product_info_keys:
            k = product_info_key.find('th')
            list_keys.append(k.text)    
    
  for product_info_value in product_info_values:
            v = product_info_value.find('td')
            list_values.append(v.text) 

 
  product_info = [
                    {"title": title.text},
                    {"category": category},  
                    {"review_rating" : review_rating[1]}, 
                    {"image_url" : image_url},
                    {list_keys[0]: list_values[0]},                
                    {list_keys[1]: list_values[1]},
                    {list_keys[2]: list_values[2]},
                    {list_keys[3]: list_values[3]},
                    {list_keys[4]: list_values[4]},
                    {list_keys[5]: list_values[5]},
                    {list_keys[6]: list_values[6]}
                  ]

                 
#File csv          

  articles = ["keys", "values"]
  with open('infos.csv', 'w') as files_csv:
     writer = csv.writer(files_csv, delimiter=',')
     writer.writerow(articles)
     for product_info_key, product_info_value in zip(list_keys, list_values):         
       writer.writerow([product_info_key,product_info_value])

  return product_info                 



"""
Écrivez un script Python qui consulte la page de la catégorie choisie,
et extrait l'URL de la page Produit de chaque livre appartenant à cette catégorie
"""


url = 'https://books.toscrape.com/catalogue/category/books/travel_2/index.html'
page = requests.get(url)
soup = BeautifulSoup(page.content,'html.parser')

def get_books_links_one_categorie(): 
    lienProductInfo = []
    liens = soup.findAll('div',{'class':'image_container'})
    for i in liens:
        a = i.find('a')
        link = a['href']
        lienProductInfo.append(link.replace('../../../','https://books.toscrape.com/catalogue/'))    
    return lienProductInfo  


#extraire les données produit de tous les livres de la catégorie choisie, puis écrivez les données dans un seul fichier CSV.
    


def get_products(lienProductInfo):
    
    list_catalogue_product = []
      
    for x in range(len(lienProductInfo)):
          url6 = lienProductInfo[x]  
          page6 = requests.get(url6)
          soup6 = BeautifulSoup(page6.content,'html.parser') 
                  
          
          images = soup6.find('div',{'class':'carousel-inner'}).find('div',{'class':'item active'})
          t = images.find('img')
          w = t['src']

          titleBook = soup6.find('ul',{'class':'breadcrumb'}).find('li',{'class':'active'}) 
          books = soup6.find('ul',{'class':'breadcrumb'}).findAll('li') 
          product = soup6.findAll('th')
          product2 = soup6.findAll('td')
          title = soup6.find('h1')

          list_catalogue_product =  [
                                      {"url page" : lienProductInfo[x]},
                                      {"url_image" : w.replace('../../','https://books.toscrape.com/')},
                                      {"title" : titleBook.string},
                                      {product[0].text: product2[0].text},
                                      {product[1].text: product2[1].text},
                                      {product[2].text: product2[2].text},
                                      {product[3].text: product2[3].text}, 
                                      {product[4].text: product2[4].text},
                                      {product[5].text: product2[5].text},
                                      {product[6].text: product2[6].text} 

                                  ]                                

          for catalogue in list_catalogue_product:
               print(catalogue)                       

#RETURN A LIST OF EVERY CATEGORIES OF BOOKSCRAP WEBSITE
def get_categories():
    f =  soup.find('aside',{'class':'sidebar col-sm-4 col-md-3'}).find('ul').findAll('li')
    categories = []
    for i in range(1, len(f)):
        a = f[i].text.replace("\n","")
        b = a.strip()
        categories.append(b)
    return categories

#RETURN A LIST OF JPG CATEGORY (TRAVELD) 
def get_jpg():
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

# LIST: ADRESS URL OF EACH CATEGORY 
def get_url_category():
    f =  soup.find('aside',{'class':'sidebar col-sm-4 col-md-3'}).find('ul').findAll('li')
    listUrlCategorie = []
    j = 0

    for i in range (len(li)):
        j = j + 1
        a = f[j].text.replace("\n","")
        b = a.strip()
        c = b.lower()
        url1 = "https://books.toscrape.com/catalogue/category/books/"+str(c)+"_"+str(i)+"/index.html"
        page1 = requests.get(url1)
        soup1 = BeautifulSoup(page1.content,'html.parser')
        listUrlCategorie.append(url1)
        print(*listUrlCategorie,sep="\n")
  
  
    
# DOWNLOAD PICTURE ONE CATEGORIE(TRAVELD)
def get_pictures():
    f = open('picture.jpg','wb')
    response = requests.get('https://books.toscrape.com/media/cache/6d/41/6d418a73cc7d4ecfd75ca11d854041db.jpg')
    f.write(response.content)
    f.close()





                            





    



