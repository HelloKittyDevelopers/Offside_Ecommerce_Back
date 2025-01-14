from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from api.models import *
from django.db.models import Avg, Count

# serializers.py

from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.serializers import ModelSerializer, SerializerMethodField

# serializers.py

from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from api.models import *

class UserSerializer(ModelSerializer):
    name = serializers.SerializerMethodField(read_only=True)
    isAdmin = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username', 'email', 'isAdmin']
    
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
        fields = ['id', 'first_name', 'last_name', 'username', 'email', 'isAdmin', 'token']
    
    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)

class UserRegisterSerializer(serializers.ModelSerializer):
    # Define custom error messages
    email = serializers.EmailField(error_messages={'unique': 'Email already registered.'})
    username = serializers.CharField(error_messages={'unique': 'Username already exists.'})

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id_category', 'category']

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id_image', 'image']

class OrderStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderState
        fields = ['id_order_state', 'order_state']

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id_review', 'rating', 'comment', 'creation_date', 'product', 'user']

class StockSerializer(serializers.ModelSerializer):
    size = serializers.CharField(source='product_size.size_product.size')

    class Meta:
        model = Stock
        fields = ['id_stock', 'size', 'quantity']

class ProductSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    sizes = serializers.SerializerMethodField()
    images = serializers.SerializerMethodField()
    average_rating = serializers.SerializerMethodField()
    review_count = serializers.SerializerMethodField()
    type_category = serializers.PrimaryKeyRelatedField(queryset=Type.objects.all())
    categories = serializers.PrimaryKeyRelatedField(many=True, queryset=Category.objects.all(), write_only=True)

    class Meta:
        model = Product
        fields = ['id_product', 'product_name', 'price', 'description', 'type_category', 'categories', 'reviews', 'sizes', 'images', 'average_rating', 'review_count']

    def get_sizes(self, obj):
        sizes = Stock.objects.filter(product_size__product_size=obj)
        return StockSerializer(sizes, many=True).data

    def get_images(self, obj):
        images = Image.objects.filter(product_image=obj)
        return ImageSerializer(images, many=True).data

    def get_average_rating(self, obj):
        reviews = Review.objects.filter(product=obj)
        return reviews.aggregate(average_rating=Avg('rating'))['average_rating'] or 0

    def get_review_count(self, obj):
        reviews = Review.objects.filter(product=obj)
        return reviews.aggregate(count=Count('id_review'))['count'] or 0

    def create(self, validated_data):
        categories = validated_data.pop('categories', [])
        product = Product.objects.create(**validated_data)
        for category in categories:
            ProductCategory.objects.create(category_product=category, product_category=product)
        return product

class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ['category_product', 'product_category']

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['id_order_item', 'order_quantity', 'product', 'order_user']

class ProductSizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSize
        fields = ['product_size', 'size_product']

class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = ['id_size', 'size']

class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ['id_type', 'type']

class OrderUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderUser
        fields = ['id_order', 'date_order', 'shipping_price', 'total_payment', 'user', 'order_state', 'taxes']
