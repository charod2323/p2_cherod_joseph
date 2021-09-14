from bs4 import BeautifulSoup
import csv
import requests

url = 'https://books.toscrape.com/catalogue/category/books/travel_2/index.html'
page = requests.get(url)
soup = BeautifulSoup(page.content,'html.parser')




def get_url_category():
  """
  Adress url of each pages category  
  """
  f =  soup.find('aside',{'class':'sidebar col-sm-4 col-md-3'}).find('ul').findAll('li')
  url_categorie = []
  j = 0
  i = 1
  for i in range (2,len(f)):
      j = j + 1
      a = f[j].text.replace("\n","")
      b = a.strip()
      c = b.lower()
      url1 = "https://books.toscrape.com/catalogue/category/books/"+str(c)+"_"+str(i)+"/index.html"
      url_categorie.append(url1)
  return url_categorie





def get_books_links_one_categorie(adress_category):
    """
    links products info
    """
    
    
    for y in range(1):
       
        url2 = adress_category[y]
        page2 = requests.get(url2)
        soup2 = BeautifulSoup(page2.content,'html.parser')
        print("")
        print(adress_category[y])
        print("")

        lien_product_info = []

        liens = soup2.findAll('div',{'class':'image_container'})
        for i in liens:
          a = i.find('a')
          link = a['href']
          lien_product_info.append(link.replace('../../../','https://books.toscrape.com/catalogue/')) 
        for i in lien_product_info:
            print("lien_product_info : ",i)

  
        
    return lien_product_info


#extraire les données produit de tous les livres de la catégorie choisie, puis écrivez les données dans un seul fichier CSV.
    


def get_products(lien_product_info):
    """
    data products infos
    """
    
    catalogue_product = []
      
    for x in range(len(lien_product_info)):
        url6 = lien_product_info[x]  
        page6 = requests.get(url6)
        soup6 = BeautifulSoup(page6.content,'html.parser') 
                  
          
        images = soup6.find('div',{'class':'carousel-inner'}).find('div',{'class':'item active'})
        t = images.find('img')
        w = t['src']

        title_book = soup6.find('ul',{'class':'breadcrumb'}).find('li',{'class':'active'}) 
        books = soup6.find('ul',{'class':'breadcrumb'}).findAll('li') 
        product = soup6.findAll('th')
        product2 = soup6.findAll('td')
        title = soup6.find('h1')

        catalogue_product =  [
                               {"url page" : lien_product_info[x]},
                               {"url_image" : w.replace('../../','https://books.toscrape.com/')},
                               {"title" : title_book.string},
                               {product[0].text: product2[0].text},
                               {product[1].text: product2[1].text},
                               {product[2].text: product2[2].text},
                               {product[3].text: product2[3].text}, 
                               {product[4].text: product2[4].text},
                               {product[5].text: product2[5].text},
                               {product[6].text: product2[6].text} 

                                  ]  



        print("")
           
                                                                              

        for catalogue in catalogue_product:
             print(catalogue)                       

                            







