from django.contrib import admin
# Register your models here.
from .models import (
    Proyecto,
    Proyecto_Usuario
)

admin.site.register(Proyecto)
admin.site.register(Proyecto_Usuario)