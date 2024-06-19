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
        # Get product with respective id
        cursor.execute("""
            SELECT * FROM api_product WHERE id_product = %s
        """, [product_id])
        product = cursor.fetchone()

        return product
    except Product.DoesNotExist:
        return None

def get_products_by_category(category_name):
    with connection.cursor() as cursor:
        # Get the category id for the given category name
        cursor.execute("""
            SELECT id_category FROM api_category WHERE category = %s
        """, [category_name])
        category_id = cursor.fetchone()
        
        if category_id is None:
            return []
        
        category_id = category_id[0]

        # Get product ids associated with the category id
        cursor.execute("""
            SELECT product_category_id FROM api_productcategory WHERE category_product_id = %s
        """, [category_id])
        product_ids = cursor.fetchall()

        # Convert list of tuples to list of ids
        product_ids = [pid[0] for pid in product_ids]

        if not product_ids:
            return []

        # Get products with the obtained product ids
        product_ids_tuple = tuple(product_ids)
        cursor.execute("""
            SELECT * FROM api_product WHERE id_product IN %s
        """, [product_ids_tuple])
        products = cursor.fetchall()
    
    return products


