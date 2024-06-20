import pytest
from django.test import TestCase
from api.db_queries import get_all_products, get_product_by_id, get_products_by_category
from api.models import Product, Category, ProductCategory

@pytest.mark.django_db
class ProductTestCase(TestCase):
    
    def setUp(self):
        # Crear categorías de prueba
        self.category = Category.objects.create(category='Ropa')
        # Crear productos de prueba
        self.product1 = Product.objects.create(name='Camisa', price=25.00)
        self.product2 = Product.objects.create(name='Pantalones', price=40.00)
        # Asociar productos a la categoría
        ProductCategory.objects.create(product_category_id=self.product1.id, category_product_id=self.category.id)
        ProductCategory.objects.create(product_category_id=self.product2.id, category_product_id=self.category.id)

    @pytest.mark.django_db
    def test_get_all_products(self):
        setUp(self)
        products = get_all_products()
        self.assertEqual(len(products), 2)
        self.assertIn(self.product1, products)
        self.assertIn(self.product2, products)

    @pytest.mark.django_db
    def test_get_product_by_id(self):
        result = get_product_by_id(self.product1.id)
        self.assertEqual(result, self.product1)

        result = get_product_by_id(999)
        self.assertIsNone(result)

    @pytest.mark.django_db
    def test_get_products_by_category(self):
        products = get_products_by_category('Ropa')
        self.assertEqual(len(products), 2)
        self.assertIn(self.product1, products)
        self.assertIn(self.product2, products)

        products = get_products_by_category('Electronica')
        self.assertEqual(len(products), 0)