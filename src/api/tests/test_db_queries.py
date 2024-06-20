import pytest
from django.test import TestCase
from api.db_queries import (
    get_all_products, get_product_by_id, get_products_by_category,
    get_products_by_type, get_products_by_price, get_products_by_size,
    get_products_by_category_by_filters
)
from api.models import Product, Category, ProductCategory

@pytest.mark.django_db
class ProductTestCase(TestCase):
    
    def setUp(self):
        # Create test categories
        self.category = Category.objects.create(category='Ropa')
        # Create test products
        self.product1 = Product.objects.create(product_name='Camisa', price=25.00)
        self.product2 = Product.objects.create(product_name='Pantalones', price=40.00)
        # Associate products with the category
        ProductCategory.objects.create(product_category_id=self.product1.id_product, category_product_id=self.category.id_category)
        ProductCategory.objects.create(product_category_id=self.product2.id_product, category_product_id=self.category.id_category)

    def test_get_all_products(self):
        super().setUp()
        products = get_all_products()
        self.assertEqual(len(products), 2)
        self.assertIn(self.product1, products)
        self.assertIn(self.product2, products)

    def test_get_product_by_id(self):
        super().setUp()
        result = get_product_by_id(self.product1.id_product)
        self.assertEqual(result, self.product1)

        result = get_product_by_id(999)
        self.assertIsNone(result)

    def test_get_products_by_category(self):
        super().setUp()
        products = get_products_by_category('Ropa')
        self.assertEqual(len(products), 2)
        self.assertIn(self.product1, products)
        self.assertIn(self.product2, products)

        products = get_products_by_category('Electronica')
        self.assertEqual(len(products), 0)
