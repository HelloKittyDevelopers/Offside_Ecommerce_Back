from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from api.models import *

# serializers.py

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username','email']

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['id_category', 'category']

class ImageSerializer(ModelSerializer):
    class Meta:
        model = Image
        fields = ['id_image', 'image', 'product_image']

class OrderStateSerializer(ModelSerializer):
    class Meta:
        model = OrderState
        fields = ['id_order_state', 'order_state']

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['id_product', 'product_name', 'price', 'description', 'type_category']

class ProductCategorySerializer(ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ['category_product', 'product_category']

class OrderItemSerializer(ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['id_order_item', 'order_quantity', 'product', 'order_user']

class ProductSizeSerializer(ModelSerializer):
    class Meta:
        model = ProductSize
        fields = ['product_size', 'size_product']

class SizeSerializer(ModelSerializer):
    class Meta:
        model = Size
        fields = ['id_size', 'size']

class StockSerializer(ModelSerializer):
    class Meta:
        model = Stock
        fields = ['id_stock', 'quantity', 'product_size']

class TypeSerializer(ModelSerializer):
    class Meta:
        model = Type
        fields = ['id_type', 'type']

class OrderUserSerializer(ModelSerializer):
    class Meta:
        model = OrderUser
        fields = ['id_order', 'date_order', 'total_payment', 'address', 'user', 'order_state', 'taxes']

class ReviewSerializer(ModelSerializer):
    class Meta:
        model = Review
        fields = ['id_review', 'rating', 'comment', 'creation_date', 'product_review', 'review_user']