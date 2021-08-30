
import requests

from bs4 import BeautifulSoup



url = 'https://books.toscrape.com/catalogue/category/books/travel_2/index.html'
page = requests.get(url)
soup = BeautifulSoup(page.content,'html.parser')




#LIST  IMAGES CATEGORY (TRAVELD) 


def get_imagejpg():
    
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
    print("")





    


    



