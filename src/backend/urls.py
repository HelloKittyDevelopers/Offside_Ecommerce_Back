from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from api.views.views import *

urlpatterns = [
    path('admin/', admin.site.urls),

    path('home/', include('api.urls')),  # Incluir las rutas de home

    path('users/login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),

    path('users/register/', RegisterUserView.as_view(), name='register'),

    path('users/profile/', UserProfileView.as_view(), name="users-profile"),  

    path('users/', getUsers.as_view(), name="users"), 

    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
