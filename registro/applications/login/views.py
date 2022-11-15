from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.views.generic import (
    View,
    CreateView,
    ListView,
    DeleteView,
    UpdateView,
)
from django.views.generic import (
    FormView,
)

from .models import User
from .forms import UserCreateForm, LoginForm, UpdatePasswordForm

class LoginView(FormView):
    template_name = 'login/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('home_app:home')
    
    def form_valid(self, form):
        user = authenticate(
            username = form.cleaned_data['username'],
            password = form.cleaned_data['password']
        )
        login(self.request, user)
        return super(LoginView, self).form_valid(form)

class UserCreateView(FormView):
    template_name = "login/add.html"
    form_class = UserCreateForm
    success_url = reverse_lazy('login_app:lista-user')
    
    def form_valid(self, form):
        
        User.objects.create_user(
            form.cleaned_data['username'],
            form.cleaned_data['password'],
            nombre=form.cleaned_data['nombre'],
            apellido=form.changed_data['apellido'],
        )
        
        return super(UserCreateView, self).form_valid(form)

class UserListView(ListView):
    template_name = "login/lista.html"
    context_object_name = 'usuario'
       
    def get_queryset(self):
        return User.objects.all()
    

class UserDeleteView(DeleteView):
    model = User
    template_name = "login/eliminar.html"
    success_url = reverse_lazy('login_app:lista-user')
    

class UserUpdateView(UpdateView):
    model = User
    template_name = "login/update.html"
    fields = [
        'username',
        'nombre',
        'apellido',
        'telefono',
        'mail',
        'tipo',
        'password',
    ]
    success_url = reverse_lazy('login_app:lista-user')

class User2UpdateView(UpdateView):
    model = User
    template_name = "login/update2.html"
    fields = [
        'activo'
    ]
    success_url = reverse_lazy('login_app:lista-user')
    
class LogoutView(View):
    
    def get(self, request, *args, **kargs):
        logout(request)
        return HttpResponseRedirect(
            reverse(
                'login_app:login'
            )
        )
        
class PasswordUpdateView(LoginRequiredMixin, FormView):
    template_name = 'login/passwordupdate.html'
    form_class = UpdatePasswordForm
    success_url = reverse_lazy('login_app:login')
    login_url = reverse_lazy('login_app:login')
    
    def form_valid(self, form):
        usuario = self.request.user
        user = authenticate(
            username = usuario.username,
            password = form.cleaned_data['password1']
        )
        if user:
            new_password = form.cleaned_data['password2']
            usuario.set_password(new_password)
            usuario.save()
            
        logout(self.request)
        return super(PasswordUpdateView, self).form_valid(form)