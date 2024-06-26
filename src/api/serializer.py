from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from api.models import *

# serializers.py

class UserSerializer(ModelSerializer):
    name = serializers.SerializerMethodField(read_only=True)
    isAdmin = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'name', 'isAdmin']
    
    def get_isAdmin(self, obj):
        return obj.is_staff
    
    def get_name(self, obj):
        name = obj.first_name
        if name == '':
            name = obj.email
        return name

class UserSerializerWithToken(UserSerializer):
    token = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'name', 'isAdmin', 'token']
    
    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)
    

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