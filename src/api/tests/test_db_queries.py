import pytest
from django.test import TestCase
from api.db_queries import (
    get_all_products, get_product_by_id, get_product_images, get_products_by_category,
    get_products_by_type, get_products_by_price, get_products_by_size,
    get_products_by_category_by_filters, get_all_categories, get_all_types, get_all_sizes
)
from api.models import Product, Category, ProductCategory, Type, Size, ProductSize, Image

@pytest.mark.django_db
class ProductTestCase(TestCase):

    def setUp(self):
        # Create test categories
        self.category = Category.objects.create(category='Ropa')
        self.category_shoes = Category.objects.create(category='Zapatos')
        
        # Create test types
        self.type_formal = Type.objects.create(type='Formal')
        self.type_casual = Type.objects.create(type='Casual')
        
        # Create test sizes
        self.size_m = Size.objects.create(size='M')
        self.size_xxl = Size.objects.create(size='XXL')
        
        # Create test products
        self.product1 = Product.objects.create(product_name='Camisa', price=25.00, type_category=self.type_casual)
        self.product2 = Product.objects.create(product_name='Pantalones', price=40.00, type_category=self.type_formal)
        
        # Associate products with the category
        ProductCategory.objects.create(product_category_id=self.product1.id_product, category_product_id=self.category.id_category)
        ProductCategory.objects.create(product_category_id=self.product2.id_product, category_product_id=self.category.id_category)
        
        # Associate products with sizes
        ProductSize.objects.create(product_size_id=self.product1.id_product, size_product_id=self.size_m.id_size)
        
        # Create test images
        self.image1 = Image.objects.create(product_image=self.product1, image=b'somebinarydata')
        
    def test_get_all_products(self):
        products = get_all_products()
        self.assertEqual(len(products), 2)
        self.assertIn(self.product1, products)
        self.assertIn(self.product2, products)

    def test_get_product_by_id(self):
        result = get_product_by_id(self.product1.id_product)
        self.assertEqual(result, self.product1)

        result = get_product_by_id(999)
        self.assertIsNone(result)

    def test_get_product_images(self):
        images = get_product_images(self.product1.id_product)
        self.assertEqual(len(images), 1)
        self.assertEqual(images[0], self.image1)

        images = get_product_images(999)
        self.assertEqual(len(images), 0)

    def test_get_products_by_category(self):
        products = get_products_by_category('Ropa')
        self.assertEqual(len(products), 2)
        self.assertIn(self.product1, products)
        self.assertIn(self.product2, products)

        products = get_products_by_category('Electronica')
        self.assertEqual(len(products), 0)

    def test_get_products_by_type(self):
        products = get_products_by_category('Ropa')
        filtered_products = get_products_by_type(products, 'Formal')
        self.assertEqual(len(filtered_products), 1)
        self.assertIn(self.product2, filtered_products)

        filtered_products = get_products_by_type(products, 'Deportivo')
        self.assertEqual(len(filtered_products), 0)

    def test_get_products_by_price(self):
        products = get_products_by_category('Ropa')
        filtered_products = get_products_by_price(products, 10, 50)
        self.assertEqual(len(filtered_products), 2)
        self.assertIn(self.product1, filtered_products)
        self.assertIn(self.product2, filtered_products)

        filtered_products = get_products_by_price(products, 100, 200)
        self.assertEqual(len(filtered_products), 0)

    def test_get_products_by_size(self):
        products = get_products_by_category('Ropa')
        filtered_products = get_products_by_size(products, 'M')
        self.assertEqual(len(filtered_products), 1)
        self.assertIn(self.product1, filtered_products)

        filtered_products = get_products_by_size(products, 'XXL')
        self.assertEqual(len(filtered_products), 0)

    def test_get_products_by_category_by_filters(self):
        filtered_products = get_products_by_category_by_filters('Ropa', 'Casual', 10, 50, 'M')
        self.assertEqual(len(filtered_products), 1)
        self.assertIn(self.product1, filtered_products)

        filtered_products = get_products_by_category_by_filters('Pantalones', 'Formal', 100, 150, 'L')
        self.assertEqual(len(filtered_products), 0)

    def test_get_all_categories(self):
        categories = get_all_categories()
        self.assertEqual(len(categories), 2)
        self.assertIn(self.category, categories)
        self.assertIn(self.category_shoes, categories)

    def test_get_all_types(self):
        types = get_all_types()
        self.assertEqual(len(types), 2)
        self.assertIn(self.type_formal, types)
        self.assertIn(self.type_casual, types)

    def test_get_all_sizes(self):
        sizes = get_all_sizes()
        self.assertEqual(len(sizes), 2)
        self.assertIn(self.size_m, sizes)
        self.assertIn(self.size_xxl, sizes)
