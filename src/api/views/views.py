from django.shortcuts import render
from rest_framework import generics
from api.models import *
from api.serializer import *
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import viewsets
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from api.db_queries import *
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from django.db.models import Avg, Count

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
class ProductDetailView(generics.RetrieveAPIView):
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]

    def get_object(self):
        product_id = self.kwargs['pk']
        return get_object_or_404(Product, pk=product_id)

    def get(self, request, *args, **kwargs):
        product = self.get_object()
        serializer = self.get_serializer(product)
        
        reviews = Review.objects.filter(product_id=product.id)
        review_average = reviews.aggregate(average_rating=Avg('rating'))['average_rating'] or 0
        review_count = reviews.aggregate(count=Count('id_review'))['count'] or 0
        reviews_serializer = ReviewSerializer(reviews, many=True)
        
        data = serializer.data
        data['reviews'] = reviews_serializer.data
        data['average_rating'] = review_average
        data['review_count'] = review_count

        return Response(data)
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
