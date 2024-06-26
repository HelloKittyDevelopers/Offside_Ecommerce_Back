from api.models import *
from api.serializer import *
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework import viewsets
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.views import APIView
from django.contrib.auth.hashers import make_password
from rest_framework import status


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    
    def validate(self, attrs):
        data = super().validate(attrs)

        serializer = UserSerializerWithToken(self.user).data

        for k, v in serializer.items():
            data[k] = v

        return data    

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class RegisterUserView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        data = request.data

        try:
            user = User.objects.create(
                first_name = data['first_name'],
                last_name = data['last_name'],
                username=data['username'],
                email=data['email'],
                password=make_password(data['password'])
            )
        except: 
            message = {'detail' : 'El usuario con este email ya existe'}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)

        serializer = UserSerializerWithToken(user, many=False)
        return Response(serializer.data)


class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
class getUsers(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

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
