from dataclasses import field
from  rest_framework import serializers

from .models import Proyecto, Proyecto_Usuario

class ProyectoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proyecto
        fields = (
            'id',
            'nombre',
            'activo',
        )
        
class ProyectoUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proyecto
        fields = (
            'nombre',
        )
        
class ProyectoUpdate2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Proyecto
        fields = (
            'activo',
        )
        
class ProyectoUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proyecto_Usuario
        fields = (
            'id',
            'proyecto_id',
            'user_id',
            'activo',
        )
        
class ProyectoUserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proyecto_Usuario
        fields = (
            'id',
            'proyecto_id',
            'user_id',
        )
        
class ProyectoUserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proyecto_Usuario
        fields = (
            'proyecto_id',
            'user_id',
        )