import csv
import requests

from bs4 import BeautifulSoup

url = 'https://books.toscrape.com/catalogue/category/books/travel_2/index.html'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')


def get_categories_url():
    """
    Adress url of each pages category
    """

    f = soup.find('aside', {'class': 'sidebar col-sm-4 col-md-3'}).find('ul').findAll('li')
    url_categorie = []
    j = 0
    i = 1
    for i in range(2, len(f) + 1):
        j = j + 1
        a = f[j].text.replace("\n", "")
        b = a.strip()
        c = b.lower()
        url1 = "https://books.toscrape.com/catalogue/category/books/" + str(c) + "_" + str(i) + "/index.html"
        url_categorie.append(url1)
    return url_categorie


def get_books_url_of_category(url):
    """
    Return all books of one category with url given.
    """
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    links = soup.findAll('div', {'class': 'image_container'})
    book_urls = []
    for link in links:
        a = link.find('a')
        href = a['href']
        book_urls.append(href.replace('../../../', 'https://books.toscrape.com/catalogue/'))
    return book_urls


def get_books_links_one_categorie(adress_category):
    """
    Links products info
    """
    for y in range(1):

        url2 = adress_category[y]
        page2 = requests.get(url2)
        soup2 = BeautifulSoup(page2.content, 'html.parser')
        print("")
        print(adress_category[y])
        print("")

        lien_product_info = []

        liens = soup2.findAll('div', {'class': 'image_container'})
        for i in liens:
            a = i.find('a')
            link = a['href']
            lien_product_info.append(link.replace('../../../', 'https://books.toscrape.com/catalogue/'))
        for i in lien_product_info:
            print("lien_product_info : ", i)
    return lien_product_info


def get_product_info(book_url):
    """
    Return all data products infos.
    """
    page = requests.get(book_url)
    soup = BeautifulSoup(page.content, 'html.parser')

    images = soup.find('div', {'class': 'carousel-inner'}).find('div', {'class': 'item active'})
    t = images.find('img')
    w = t['src']
    pictures = w.replace('../../', 'https://books.toscrape.com/')
    count = 0
    title_book = soup.find('ul', {'class': 'breadcrumb'}).find('li', {'class': 'active'})
    books = soup.find('ul', {'class': 'breadcrumb'}).findAll('li')
    product = soup.findAll('th')
    product2 = soup.findAll('td')
    title = soup.find('h1')

    catalogue_product = {
        'url page': book_url,
        "url_image": pictures,
        'title': title_book.string,
        product[0].text: product2[0].text,
        product[1].text: product2[1].text,
        product[2].text: product2[2].text,
        product[3].text: product2[3].text,
        product[4].text: product2[4].text,
        product[5].text: product2[5].text,
        product[6].text: product2[6].text
    }
    
    # Download image
    data_name_img = []
    date_name_title = []

    data_name_img.append(catalogue_product["url_image"])
    date_name_title.append(catalogue_product["title"])

    name_img = catalogue_product["title"]
    f = open(name_img, 'wb')
    response = requests.get(catalogue_product["url_image"])
    f.write(response.content)
    f.close()

    # TODO: Download image of current product (catalogue_product['url_image'])
    print("catalogue_product['url_image']", catalogue_product['url_image'])

    return catalogue_product    

def get_csv(prod):
    """
    Creation csv
    """
    for categorys in prod:           
        title_file = ['product_information']
        with open('files','w') as product_files:
             writer = csv.writer(product_files,delimiter= ',')
             writer.writerow(title_file)
             for categorys in zip(prod):
                 writer.writerow([categorys])
