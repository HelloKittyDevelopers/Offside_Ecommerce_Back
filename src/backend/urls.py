# backend/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from api.views.views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('home/', include('api.urls')),  # Incluir las rutas de home

    path('users/login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),

    path('users/register/', RegisterUserView.as_view(), name='register'),

    path('users/profile/', UserProfileView.as_view(), name="users-profile"),  

    path('users/', getUsers.as_view(), name="users"), 

    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]


# Adding media files route in development mode
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
