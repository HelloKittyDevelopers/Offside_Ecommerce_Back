from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

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

    class Meta:
        model = Product
        fields = ['id_product', 'product_name', 'price', 'description', 'type_category', 'reviews', 'sizes', 'images']

    def get_sizes(self, obj):
        sizes = Stock.objects.filter(product_size__product_size=obj)
        return StockSerializer(sizes, many=True).data

    def get_images(self, obj):
        images = Image.objects.filter(product_image=obj)
        return ImageSerializer(images, many=True).data

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
        fields = ['id_order', 'date_order', 'total_payment', 'address', 'user', 'order_state', 'taxes']
