from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    ListView,
    DeleteView,
    UpdateView,
    TemplateView,
)

from .models import Proyecto, Proyecto_Usuario

class HomeView(TemplateView):
    template_name = "home/home.html"

class ProyectoCreateView(CreateView):
    model = Proyecto
    template_name = "home/add.html"
    fields = ('__all__')
    success_url = reverse_lazy('home_app:lista')

class ProyectoListView(ListView):
    template_name = "home/lista.html"
    context_object_name = 'proyecto'
       
    def get_queryset(self):
        return Proyecto.objects.all()
    

class ProyectoDeleteView(DeleteView):
    model = Proyecto
    template_name = "home/eliminar.html"
    success_url = reverse_lazy('home_app:lista')
    

class ProyectoUpdateView(UpdateView):
    model = Proyecto
    template_name = "home/update.html"
    fields = [
        'nombre'
    ]
    success_url = reverse_lazy('home_app:lista')

class Proyecto2UpdateView(UpdateView):
    model = Proyecto
    template_name = "home/update2.html"
    fields = [
        'activo'
    ]
    success_url = reverse_lazy('home_app:lista')

class ProyectoUserListView(ListView):
    template_name = "home/proyectouserlista.html"
    context_object_name = 'proyecto_user'
       
    def get_queryset(self):
        return Proyecto_Usuario.objects.all()
    
class ProyectoUserCreateView(CreateView):
    model = Proyecto_Usuario
    template_name = "home/proyectouseradd.html"
    fields = ('__all__')
    success_url = reverse_lazy('home_app:list-proyecto-user')
    
class ProyectoUserUpdateView(UpdateView):
    model = Proyecto_Usuario
    template_name = "home/proyectouserupdate.html"
    fields = [
        'proyecto_id',
        'user_id',
    ]
    success_url = reverse_lazy('home_app:list-proyecto-user')