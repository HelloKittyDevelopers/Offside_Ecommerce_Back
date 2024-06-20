# api/views.py
from django.shortcuts import render
from rest_framework import generics
from api.models import *
from api.serializer import *
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import viewsets

# Create views
class CreateUserView(generics.CreateAPIView):
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer
    permission_classes = [AllowAny]

class CreateRol(generics.CreateAPIView):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer
    permission_classes = [AllowAny]

class ProductView(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [AllowAny]

class CategoryView(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [AllowAny]

class ImageView(viewsets.ModelViewSet):
    serializer_class = ImageSerializer
    queryset = Image.objects.all()
    permission_classes = [AllowAny]

class OrderStateView(viewsets.ModelViewSet):
    serializer_class = OrderStateSerializer
    queryset = OrderState.objects.all()
    permission_classes = [AllowAny]

class UserInfoView(viewsets.ModelViewSet):
    serializer_class = UserInfoSerializer
    queryset = UserInfo.objects.all()
    permission_classes = [AllowAny]

class ProductCategoryView(viewsets.ModelViewSet):
    serializer_class = ProductCategorySerializer
    queryset = ProductCategory.objects.all()
    permission_classes = [AllowAny]

class ProductOrderView(viewsets.ModelViewSet):
    serializer_class = ProductOrderSerializer
    queryset = ProductOrder.objects.all()
    permission_classes = [AllowAny]

class ProductSizeView(viewsets.ModelViewSet):
    serializer_class = ProductSizeSerializer
    queryset = ProductSize.objects.all()
    permission_classes = [AllowAny]

class RolView(viewsets.ModelViewSet):
    serializer_class = RolSerializer
    queryset = Rol.objects.all()
    permission_classes = [AllowAny]

class SizeView(viewsets.ModelViewSet):
    serializer_class = SizeSerializer
    queryset = Size.objects.all()
    permission_classes = [AllowAny]

class StockView(viewsets.ModelViewSet):
    serializer_class = StockSerializer
    queryset = Stock.objects.all()
    permission_classes = [AllowAny]

class TypeView(viewsets.ModelViewSet):
    serializer_class = TypeSerializer
    queryset = Type.objects.all()
    permission_classes = [AllowAny]

class OrderUserView(viewsets.ModelViewSet):
    serializer_class = OrderUserSerializer
    queryset = OrderUser.objects.all()
    permission_classes = [AllowAny]