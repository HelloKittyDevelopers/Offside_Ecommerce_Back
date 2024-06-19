# db_queries.py

from .models import (
    Category, Image, OrderState, UserInfo, Product,
    ProductCategory, ProductOrder, ProductSize, Rol, Size,
    Stock, Type, UserRol, OrderUser
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

def get_products_by_category_and_filters(type, min_price, max_price, size):
    with connection.cursor() as cursor:


