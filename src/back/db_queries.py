# db_queries.py

from .models import (
    Category, Image, OrderState, UserInfo, Product,
    ProductCategory, ProductOrder, ProductSize, Rol, Size,
    Stock, Type, UserRol, OrderUser
)
from django.core.exceptions import ObjectDoesNotExist

# Product Functions
def get_all_products():
    return Product.objects.all()

def get_product_by_id(product_id):
    try:
        return Product.objects.get(id_product=product_id)
    except Product.DoesNotExist:
        return None

def get_products_by_category(category_name):
    Category.objects.filter(catergory = category_name)
    return Product.objects.filter(
        id_product__in=ProductCategory.objects.filter(category_product_id=category_id).values('product_category_id')
    )

