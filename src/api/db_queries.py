from .models import (
    Category, Image, OrderState, Product,
    ProductCategory, OrderItem, ProductSize, Size,
    Stock, Type, OrderUser, Review
)
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Count
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


def get_products_by_category(products, category_name):
    # Get the Category object by category name
    category = Category.objects.filter(category=category_name).first()
    if not category:
        return Product.objects.none()

    # Filter products by category_id using Django ORM
    category_id = category.id_category
    filtered_products = products.filter(productcategory__category_product_id=category_id)

    return filtered_products

def get_products_by_type(type_name):
    try:
        # Get the type object for the given type name
        type_obj = Type.objects.get(type=type_name)
        
        # Retrieve products filtered by type
        filtered_products = Product.objects.filter(type_category=type_obj)
        
        return filtered_products
    
    except Type.DoesNotExist:
        return Product.objects.none()

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
    filtered_products = Product.objects.raw(query, [tuple(product_ids), size_id])
    return filtered_products

def get_products_by_category_by_filters(category_name, type_name, min_price, max_price, size_name):

    products = get_products_by_type(type_name)

    if category_name is not None:
        products = get_products_by_category(products, category_name)
    
    if min_price is not None or max_price is not None:
        products = get_products_by_price(products, min_price, max_price)
    
    if size_name is not None:
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
    query ="""
        SELECT AVG(rating) AS average_rating FROM api_review WHERE product_id = %s
    """
    average_rating = Review.objects.raw(query, [product_id])[0].average_rating

    return average_rating

def get_product_review_count(product_id):
    review_count = Review.objects.filter(product_id=product_id).aggregate(count=Count('id_review'))['count']
    return review_count
