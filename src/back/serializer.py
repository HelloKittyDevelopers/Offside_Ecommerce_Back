from rest_framework.serializers import ModelSerializer

from .models import *

# serializers.py

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

class UserInfoSerializer(ModelSerializer):
    class Meta:
        model = UserInfo
        fields = ['id_user', 'username', 'encrypted_password', 'user_name', 'email', 'phone_number']

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['id_product', 'product_name', 'price', 'description', 'type_category']

class ProductCategorySerializer(ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ['category_product', 'product_category']

class ProductOrderSerializer(ModelSerializer):
    class Meta:
        model = ProductOrder
        fields = ['product_order', 'order_product']

class ProductSizeSerializer(ModelSerializer):
    class Meta:
        model = ProductSize
        fields = ['product_size', 'size_product']

class RolSerializer(ModelSerializer):
    class Meta:
        model = Rol
        fields = ['id_rol', 'rol']

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

class UserRolSerializer(ModelSerializer):
    class Meta:
        model = UserRol
        fields = ['user', 'rol']

class OrderUserSerializer(ModelSerializer):
    class Meta:
        model = OrderUser
        fields = ['id_order', 'date_order', 'total_payment', 'address', 'user', 'order_state', 'taxes']
