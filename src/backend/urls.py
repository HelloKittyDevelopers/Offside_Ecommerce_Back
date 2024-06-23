from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from api.views.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('api.urls')),  # Incluir las rutas de home
    path('api/users/profile/', UserProfileView.as_view(), name="users-profile"),  
    path('api/token/login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
