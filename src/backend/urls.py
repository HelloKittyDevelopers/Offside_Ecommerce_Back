# backend/urls.py

from django.urls import path
from api.views import views

urlpatterns = [
    path('users/', views.UserInfoListCreate.as_view(), name='user-list-create'),
    path('users/<int:pk>/', views.UserInfoDetail.as_view(), name='user-detail'),

    path('roles/', views.RolListCreate.as_view(), name='rol-list-create'),
    path('roles/<int:pk>/', views.RolDetail.as_view(), name='rol-detail'),
]
