# api/views.py

from django.shortcuts import render
from rest_framework import generics
from api.models import UserInfo, Rol
from api.serializer import UserInfoSerializer, RolSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny

# Create views

class CreateUserView(generics.CreateAPIView):
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer
    permission_classes = [AllowAny]

class CreateRol(generics.CreateAPIView):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer
    permission_classes = [AllowAny]
    

