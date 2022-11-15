from django.db import models
from applications.login.models import User

class Proyecto(models.Model):
    
    nombre = models.CharField('nombre', max_length=100,)
    activo = models.BooleanField(default=True)
    
    def __str__(self):
        return str(self.id) + '-' + self.nombre
    
class Proyecto_Usuario(models.Model):
    
    proyecto_id = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    activo = models.BooleanField(default=True)
    
    def __str__(self):
        return str(self.id) + '-' + self.proyecto_id.nombre + '-' + self.user_id.username