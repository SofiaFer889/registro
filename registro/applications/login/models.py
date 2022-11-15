from django.db import models

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .managers import UserManagers

admin = 'o'
superusuario = '1'

tipo_choice = [
    (0, 'admin'),
    (1, 'superusuario'),
]

class User(AbstractBaseUser, PermissionsMixin):
    
    username = models.CharField('username', max_length=10, unique=True)
    nombre = models.CharField('nombre', max_length=40,)
    apellido = models.CharField('apellido', max_length=40,)
    telefono = models.IntegerField(null=True)
    mail = models.EmailField(max_length=100,blank=True)
    tipo = models.IntegerField(choices=tipo_choice, null=True)
    activo = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)    
    USERNAME_FIELD = 'username'
    
    objects = UserManagers()
    
    def __str__(self):
        return self.username
    