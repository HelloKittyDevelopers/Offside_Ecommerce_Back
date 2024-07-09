from api.models import *
from api.serializer import *
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework import viewsets
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import generics
from django.shortcuts import get_object_or_404
from django.db.models import Avg, Count
from django.shortcuts import render
from django.contrib.auth.hashers import make_password
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from dj_rest_auth.registration.views import SocialLoginView  # Actualización
from rest_framework.views import APIView


class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter

class GoogleLoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        token = request.data.get('access_token')
        try:
            adapter = GoogleOAuth2Adapter()
            app = adapter.get_provider().get_app(request)
            token = adapter.parse_token({'access_token': token})
            token.app = app
            login = adapter.complete_login(request, app, token, response=None)
            login.token = token
            login.state = SocialLoginView.State.SUCCEEDED
            login.save(request, connect=True)
            user = login.user
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            # Aquí se genera el token de autenticación y se devuelve junto con los datos del usuario
            from rest_framework.authtoken.models import Token
            token, _ = Token.objects.get_or_create(user=user)
            return Response({
                'token': token.key,
                'user': {
                    'id': user.id,
                    'username': user.username,
                    'email': user.email,
                }
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        
        serializer = UserSerializerWithToken(self.user).data
        for k, v in serializer.items():
            data[k] = v
        
        return data    

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')

        try:
            user = User.objects.get(username=username)
            if user.check_password(password):
                response = super().post(request, *args, **kwargs)
                response.data['message'] = 'Logged in successfully'
                return response
            else:
                return Response({'message': 'Invalid username or password'}, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response({'message': 'Invalid username or password'}, status=status.HTTP_400_BAD_REQUEST)

class RegisterUserView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        
        if serializer.is_valid():
            # Check if user or email already exists
            username = serializer.validated_data['username']
            email = serializer.validated_data['email']
            if User.objects.filter(username=username).exists():
                return Response({'error': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)
            if User.objects.filter(email=email).exists():
                return Response({'error': 'Email already registered'}, status=status.HTTP_400_BAD_REQUEST)

            # If user and email are unique, save the user
            user = serializer.save()

            # Return success message along with user data
            return Response({
                'success': 'User registered successfully',
                'user': serializer.data,
            }, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': 'Email or  username already registered'}, status=status.HTTP_400_BAD_REQUEST)
        

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
    
class ProductDetailView(generics.RetrieveAPIView):
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]

    def get_object(self):
        product_id = self.kwargs['pk']
        return get_object_or_404(Product, pk=product_id)

    def get(self, request, *args, **kwargs):
        product = self.get_object()
        serializer = self.get_serializer(product)

        reviews = Review.objects.filter(product_id=product.id_product)
        review_average = reviews.aggregate(average_rating=Avg('rating'))['average_rating'] or 0
        review_count = reviews.aggregate(count=Count('id_review'))['count'] or 0

        images = Image.objects.filter(product_image=product)
        images_serializer = ImageSerializer(images, many=True)

        data = serializer.data
        data['average_rating'] = review_average
        data['review_count'] = review_count
        data['images'] = images_serializer.data

        return Response(data)

class ProductListingView(generics.ListAPIView):
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]

class ProductListingView(generics.ListAPIView):
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        type_name = self.kwargs['type']
        category_name = self.request.query_params.get('category', None)
        min_price = self.request.query_params.get('min_price', None)
        max_price = self.request.query_params.get('max_price', None)
        size_name = self.request.query_params.get('size', None)

        if all(param is None or param == '' for param in [category_name, min_price, max_price, size_name]):
            # Handle case where all params are None or empty
            products = get_products_by_type(type_name)
        else:
            if min_price is not None:
                min_price = float(min_price)
            if max_price is not None:
                max_price = float(max_price)

            products = get_products_by_category_by_filters(category_name, type_name, min_price, max_price, size_name)

        return products

    def list(self, request, *args, **kwargs):
        try:
            queryset = self.get_queryset()
            serializer = self.get_serializer(queryset, many=True)
            data = serializer.data

            # Add average_rating and review_count to each product
            for product_data in data:
                product_id = product_data['id_product']
                reviews = Review.objects.filter(product_id=product_id)
                review_average = reviews.aggregate(average_rating=Avg('rating'))['average_rating'] or 0
                review_count = reviews.aggregate(count=Count('id_review'))['count'] or 0

                product_data['average_rating'] = review_average
                product_data['review_count'] = review_count

            # Fetch all categories and sizes
            categories = Category.objects.all()
            sizes = Size.objects.all()

            # Serialize categories and sizes
            category_serializer = CategorySerializer(categories, many=True)
            size_serializer = SizeSerializer(sizes, many=True)

            # Append categories and sizes to the response data
            response_data = {
                'products': data,
                'categories': category_serializer.data,
                'sizes': size_serializer.data
            }

            return Response(response_data)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

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
    serializer_class = ProductCategorySerializer 
    queryset = ProductCategory.objects.all()
    permission_classes = [AllowAny]


class OrderItemView(viewsets.ModelViewSet):
    serializer_class = OrderItemSerializer
    queryset = OrderItem.objects.all()
    permission_classes = [AllowAny]

    def get_queryset(self):
        order_id = self.request.query_params.get('order_id', None)
        if order_id is not None:
            return OrderItem.objects.filter(order_user__id_order=order_id)
        return super().get_queryset()


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
