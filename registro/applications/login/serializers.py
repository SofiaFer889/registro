from dataclasses import field
from  rest_framework import serializers

from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'nombre',
            'apellido',
            'telefono',
            'mail',
            'activo',
            'tipo',
            'password',
        )
        
class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'nombre',
            'activo',
            'tipo',
        )
        
class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'nombre',
            'apellido',
            'telefono',
            'mail',
            'tipo',
            'password',
        )
        
class UserUpdate2Serializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'activo',
        )
         