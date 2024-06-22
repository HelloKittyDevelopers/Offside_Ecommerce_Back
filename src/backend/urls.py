# backend/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from api.views.views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    # path("api/user/register/", CreateUserView.as_view(), name="register"),
    # path("api/user/register/rol", CreateRol.as_view(), name="rol"),
    # path("api/token/", TokenObtainPairView.as_view(), name="get_token"),
    # path("api/token/refresh", TokenRefreshView.as_view(), name="refresh"),
    # path("api-auth", include("rest_framework.urls")),
    path("admin/", admin.site.urls),
    path("home/", include('api.urls')),
]


# Adding media files route in development mode
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)