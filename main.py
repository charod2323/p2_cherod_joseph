from utils import  (
    get_categories, get_jpg, books_of_category, get_product_info,
    get_books_links_one_categorie, get_images_titles_urls_product_info_of_one_categorie,
    get_url_category
)


from pictures import get_imagejpg


# RETRIEVE ALL CATEGORIES
categories = get_categories()
for category in categories:
    print('category:', category)

# #LIST PICTURE ONE CATEGORIE (TRAVELD)
# list_jpg_travel_categorie = get_jpg()


# GET EVERY BOOKS OF every categories
for category_url in categories:
    books = books_of_category(category_url)


# #GET PRODUCT INFO ONE BOOK
# list_product_info = get_product_info('https://books.toscrape.com/catalogue/its-only-the-himalayas_981/index.html')


# #GET BOOKS LINKS ONE CATEGORIE (TRAVELD)
# list_books_links_one_categorie = get_books_links_one_categorie()

# #GET PRODUCT INFO ALL BOOKS ONE CATEGORIE
# list_product_info_books_one_categorie = get_images_titles_urls_product_info_of_one_categorie()

# #GET ADRESS URL OF EACH CATEGORY
# list_adress_category = get_url_category()
