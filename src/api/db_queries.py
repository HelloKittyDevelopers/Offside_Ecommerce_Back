# db_queries.py

from .models import (
    Category, Image, OrderState, UserInfo, Product,
    ProductCategory, OrderItem, ProductSize, Rol, Size,
    Stock, Type, OrderUser, Review
)
from django.core.exceptions import ObjectDoesNotExist
from django.db import connection

# Product Functions
def get_all_products():
    return Product.objects.all()

def get_product_by_id(product_id):
    try:
        query = """
            SELECT * FROM api_product WHERE id_product = %s
        """
        product = Product.objects.raw(query, [product_id])
        return product[0] if product else None
    except Product.DoesNotExist:
        return None

def get_product_images(product_id):
    query = """
        SELECT *
        FROM api_image 
        WHERE product_image_id = %s
    """
    images = Image.objects.raw(query, [product_id])

    return images


def get_products_by_category(category_name):
    # Get the category id for the given category name
    category = Category.objects.filter(category=category_name).first()
    if not category:
        return Product.objects.none()
    
    category_id = category.id_category

    # Get products associated with the category id using raw SQL with parameters
    query = """
        SELECT p.*
        FROM api_product AS p
        JOIN api_productcategory AS pc ON p.id_product = pc.product_category_id
        WHERE pc.category_product_id = %s
    """
    products = Product.objects.raw(query, [category_id])
    return products

def get_products_by_type(products, type_name):
    # Get the type id for the given type name
    type_obj = Type.objects.filter(type=type_name).first()
    if not type_obj:
        return Product.objects.none()
    
    type_id = type_obj.id_type

    # Filter products by type id
    product_ids = [product.id_product for product in products]
    if not product_ids:
        return Product.objects.none()
    
    query = """
        SELECT * FROM api_product
        WHERE id_product IN %s AND type_category_id = %s
    """
    filtered_products = Product.objects.raw(query, [tuple(product_ids), type_id])
    return filtered_products

def get_products_by_price(products, min_price, max_price):
    # Filter products by price
    product_ids = [product.id_product for product in products]
    if not product_ids:
        return Product.objects.none()
    
    query = """
        SELECT * FROM api_product
        WHERE id_product IN %s AND price BETWEEN %s AND %s
    """
    if(min_price is None and max_price is not None):
        filtered_products = Product.objects.raw(query, [tuple(product_ids), 0, max_price])
    elif(min_price is not None and max_price is None):
        filtered_products = Product.objects.raw(query, [tuple(product_ids), min_price, 999999999])
    else:   
        filtered_products = Product.objects.raw(query, [tuple(product_ids), min_price, max_price])
    return filtered_products

def get_products_by_size(products, size_name):
    # Get the Size id by size name
    size = Size.objects.filter(size=size_name).first()
    if not size:
        return Product.objects.none()

    product_ids = [product.id_product for product in products]
    if not product_ids:
        return Product.objects.none()
    
    size_id = size.id_size

    # Get products associated with the size id using raw SQL with parameters
    query = """
        SELECT p.*
        FROM api_product AS p
        JOIN api_productsize AS ps ON p.id_product = ps.product_size_id
        WHERE p.id_product IN %s AND ps.size_product_id = %s
    """
    filtered_products = Product.objects.raw(query, [tuple(product_ids),size_id])
    return filtered_products

def get_products_by_category_by_filters(category_name, type_name, min_price, max_price, size_name):

    products = get_products_by_category(category_name)

    if type_name is not None:
        products = get_products_by_type(products, type_name)
    
    if(min_price is not None or max_price is not None):
        products = get_products_by_price(products, min_price, max_price)
    
    if(size_name is not None):
        products = get_products_by_size(products, size_name)
    
    return products

# Universal Functions

def get_all_categories():
    return Category.objects.all()

def get_all_types():
    return Type.objects.all()

def get_all_sizes():
    return Size.objects.all()


# Order Queries

def get_order_by_user_id(user_id):
    try:
        query = """
            SELECT * 
            FROM api_orderuser 
            WHERE user_id = %s
        """
        order = OrderUser.objects.raw(query, [user_id])
        return order[0] if order else None
    except OrderUser.DoesNotExist:
        return None


def get_all_order_products(user_id):
    # Get the order for the given user_id
    order = get_order_by_user_id(user_id)
    if not order:
        return Product.objects.none()
    
    order_id = order.id_order

    # Get products associated with the order_id using raw SQL with parameters
    query = """
        SELECT p.*
        FROM api_product AS p
        JOIN api_orderitem AS oi ON p.id_product = oi.product_id
        WHERE oi.order_user_id = %s
    """
    products = Product.objects.raw(query, [order_id])
    return products


# Product Reviews

def get_product_reviews(product_id):
    query ="""
        SELECT * FROM api_review WHERE product_id = %s
    """
    reviews = Review.objects.raw(query, [product_id])

    return reviews

def get_product_review_average(product_id):
    query = """
        SELECT AVG(rating) AS average_rating FROM api_review WHERE product_id = %s
    """
    with connection.cursor() as cursor:
        cursor.execute(query, [product_id])
        row = cursor.fetchone()
    average_rating = row[0] if row[0] is not None else None
    return float(average_rating) if average_rating is not None else None



    
