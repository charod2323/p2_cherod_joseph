
from utils import  get_categories_url, get_books_url_of_category, get_product_info, get_csv 

#GET ADRESS URL OF PAGES EACH CATEGORY

# Retrieve all categories url
category_urls = get_categories_url()

# Construct all product info for all books of all categories
products = []

# Retrieve all books info for all categorie
for i, category_url in enumerate(category_urls):

    # Retrieve all book urls for one category
    book_urls = get_books_url_of_category(category_url)

    # Retrieve all product info for each book of one category
    for book_url in book_urls:
        product_info = get_product_info(book_url)
        print('product_info:', product_info)
        products.append(product_info)
    if i == 0:
        break

print('len(products):', len(products))

get_csv(products)
# Record all into a csv file
# TODO:
# create_books_csv(products)
