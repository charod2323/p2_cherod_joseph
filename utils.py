import csv
import requests

from bs4 import BeautifulSoup


def get_categories_url():
    """
    Adress url of each pages category
    """
    url = 'https://books.toscrape.com/index.html'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    f = soup.find('aside', {'class': 'sidebar col-sm-4 col-md-3'}).find('ul').findAll('li')
    listUrlCategorie = []
    j = 0
    i = 1
    for u in range(2,len(f)+1):
        i = i + 1
        j = j + 1
        a = f[j].text.replace("\n", "")
        b = a.strip()
        v = b.lower()
        t = str(v)
        d = v.count(" ")
        if d > 0:
            c = t.replace(" ", "-")
            url0 = "https://books.toscrape.com/catalogue/category/books/" + str(c) + "_" + str(i) + "/index.html"
            listUrlCategorie.append(url0)
        else:
            url1 = "https://books.toscrape.com/catalogue/category/books/" + str(t) + "_" + str(i) + "/index.html"
            listUrlCategorie.append(url1)

    return listUrlCategorie

def all_pagination(pages):
    """
    return all pages
    """
    listUrlCategories = []
    x = 0
    w = 0

    for y in pages:
        w = w + 1
        p = "page-" + str(x + 1) + ".html"  
        url4 = pages[w - 1].replace("index.html", p)  
        page = requests.get(url4)
        soup = BeautifulSoup(page.content, 'html.parser')
        status = page.status_code
        if status == 200:
            f = soup.find('li', {'class': 'current'})
            a = str(f)
            b = a[60:61]
            c = int(b)
            for i in range(c):
                p = "page-" + str(i + 1) + ".html"
                url4 = pages[w - 1].replace("index.html", p)
                listUrlCategories.append(url4)
        else:
            listUrlCategories.append(pages[w - 1])
    return listUrlCategories


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
    name_img = catalogue_product["title"] + '.jpg'
    f = open('images :' + name_img, 'wb')
    response = requests.get(catalogue_product["url_image"])
    f.write(response.content)
    f.close()

    return catalogue_product


def create_books_csv(products):
    """
    Create a csv file containing all products of the website.
    """
    with open('csv', 'w', newline='') as csvfile:
        # Get all keys of product as header
        fieldnames = list(products[0].keys())

        writer = csv.DictWriter(csvfile, fieldnames, delimiter=',')

        writer.writeheader()

        # Add new line for each product
        for product in products:
            writer.writerow(product)





