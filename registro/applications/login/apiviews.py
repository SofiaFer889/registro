from django.shortcuts import render

from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    DestroyAPIView,
    UpdateAPIView,
)
from .models import User
from .serializers import (
    UserSerializer, 
    UserListSerializer, 
    UserUpdateSerializer,
    UserUpdate2Serializer,
)

class UsersCreateAPIView(CreateAPIView):
    
    serializer_class = UserSerializer
    
class UserListAPIView(ListAPIView):
    
    serializer_class = UserListSerializer
    
    def get_queryset(self):
        return User.objects.all()
    
class UserDestroyAPIView(DestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    
class UserUpdateAPIView(UpdateAPIView):
    serializer_class = UserUpdateSerializer
    
class UserUpdate2APIView(UpdateAPIView):
    serializer_class = UserUpdate2Serializer