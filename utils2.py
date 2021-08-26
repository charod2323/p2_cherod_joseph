
import csv

import requests

from bs4 import BeautifulSoup 

   
url = 'https://books.toscrape.com/catalogue/category/books/travel_2/index.html'
page = requests.get(url)
soup = BeautifulSoup(page.content,'html.parser')

img_list = []

#LISTE  IMAGES D UNE CATEGORIE (TRAVEL)
images = soup.findAll('div',{'class':'image_container'})

for i in images:
    t = i.find('img')
    w = t['src']
    h = w.replace('../../../../','https://books.toscrape.com/')
    img_list.append(h)
    print("\n".join(img_list))


print("")
print("")
print("")
print("")
print("")
print("")



# LIST CATEGORIE
f =  soup.find('aside',{'class':'sidebar col-sm-4 col-md-3'}).find('ul').findAll('li')

listCategorie = []

for i in range (1,51):
    a = f[i].text.replace("\n","")
    b = a.strip()
    listCategorie.append(b)
print("\n".join(listCategorie))



print("")
print("")
print("")
print("")
print("")
print("")   



# LISTE: ADRESSE URL DE CHAQUE CATEGORIE 
f =  soup.find('aside',{'class':'sidebar col-sm-4 col-md-3'}).find('ul').findAll('li')

listUrlCategorie = []
j = 0

for i in range (2,52):
    j = j + 1
    a = f[j].text.replace("\n","")
    b = a.strip()
    url = "https://books.toscrape.com/catalogue/category/books/"+str(b)+"_"+str(i)+"/index.html"
    page = requests.get(url)
    soup = BeautifulSoup(page.content,'html.parser')
    listUrlCategorie.append(url)
print(*listUrlCategorie,sep="\n")

# TITRE D UNE CATEGORIE
titresCategories = []
titreCategorie = soup.find('div',{'class':'page-header action'}).find('h1')
titresCategories.append(titreCategorie.string)
print("\n".join(titreCategorie))

#LIENS DE TOUS LES LIVRES D UNE CATEGORIES
lienProductInfo = []

liens = soup.findAll('div',{'class':'image_container'})
for i in liens:
    a = i.find('a')
    link = a['href']
    lienProductInfo.append(link.replace('../../../','https://books.toscrape.com/catalogue/'))
#print("\n".join(lienProductInfo))    


print("")
print("")
print("")
print("")
print("")
print("")  

for x in range(2):

  #AFFICHAGE PRODUCT INFOS DE TOUS LES LIVRES PAR CATEGORIE
  url6 = lienProductInfo[x]  
  page6 = requests.get(url6)
  soup6 = BeautifulSoup(page6.content,'html.parser')

  #IMAGES TITRES ET URL DE LA PAGE
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
  print("url pages: ",lienProductInfo[x])#url de la page
  print("")
  print("") 


  print("")
  print("")
  print("")
  print("")
  print("")
  print("") 

# PRODUCT INFO

for y in range(2):    
  
  books = soup6.find('ul',{'class':'breadcrumb'}).findAll('li') 
  product = soup6.findAll('th')
  product2 = soup6.findAll('td')
  title = soup6.find('h1')

  product_info = {
                   "title": title.text,
                   "category": books[2].text,                       
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

  
  
  #RETOURNE LES TITRES D'UNE CATEGORIE (TRAVELD)

titre_categorie_traveld = soup.findAll('h3') 
for t in titre_categorie_traveld:
    w = t.find('a')
    z = w['title']
    print(z)

















    


    



