from django.shortcuts import render

from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    DestroyAPIView,
    UpdateAPIView,
)
from .models import Proyecto, Proyecto_Usuario
from .serializers import (
    ProyectoSerializer,
    ProyectoUpdateSerializer,
    ProyectoUpdate2Serializer,
    ProyectoUserSerializer,
    ProyectoUserListSerializer,
    ProyectoUserUpdateSerializer,
)

class ProyectoCreateAPIView(CreateAPIView):
    
    serializer_class = ProyectoSerializer
    
class ProyectoListAPIView(ListAPIView):
    
    serializer_class = ProyectoSerializer
    
    def get_queryset(self):
        return Proyecto.objects.all()
    
class ProyectoDestroyAPIView(DestroyAPIView):
    serializer_class = ProyectoSerializer
    queryset = Proyecto.objects.all()
    
class ProyectoUpdateAPIView(UpdateAPIView):
    serializer_class = ProyectoUpdateSerializer
    
class ProyectoUpdate2APIView(UpdateAPIView):
    serializer_class = ProyectoUpdate2Serializer
    
class ProyectoUserListAPIView(ListAPIView):
    
    serializer_class = ProyectoUserListSerializer
    
    def get_queryset(self):
        return Proyecto_Usuario.objects.all()
    
class ProyectoUserCreateAPIView(CreateAPIView):
    
    serializer_class = ProyectoUserSerializer
    
class ProyectoUserUpdateAPIView(UpdateAPIView):
    serializer_class = ProyectoUserUpdateSerializer