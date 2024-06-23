from django.shortcuts import render
from rest_framework import generics
from api.models import *
from api.serializer import *
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import viewsets
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    
    def validate(self, attrs):
        data = super().validate(attrs)

        data['username'] = self.username_field
        data['email'] = self.user.email

        return data    

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class UserProfileView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
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

class ProductCategoryView(viewsets.ModelViewSet):
    serializer_class = ProductCategorySerializer  # Asegúrate de que esto esté definido en tu archivo serializer.py
    queryset = ProductCategory.objects.all()
    permission_classes = [AllowAny]

class OrderItemView(viewsets.ModelViewSet):
    serializer_class = OrderItemSerializer
    queryset = OrderItem.objects.all()
    permission_classes = [AllowAny]

class ProductSizeView(viewsets.ModelViewSet):
    serializer_class = ProductSizeSerializer
    queryset = ProductSize.objects.all()
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

class ReviewView(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()
    permission_classes = [AllowAny]
