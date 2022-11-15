from django import forms
from .models import User

class UserCreateForm(forms.ModelForm):
    password = forms.CharField(
        label='password', 
        required=True, 
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'password'
            }
        )
    )
    
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
     )
     
class LoginForm(forms.Form):
    username = forms.CharField(
        label='username', 
        required=True, 
        widget=forms.TextInput(
            attrs={
                'placeholder': 'username',
                'Style': '{ margin: 10px }',
            }
        )
    )
    
    password = forms.CharField(
        label='password', 
        required=True, 
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'password'
            }
        )
    )
    
class UpdatePasswordForm(forms.Form):
    password1 = forms.CharField(
        label='password', 
        required=True, 
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'contraseña actual'
            }
        )
    )
    password2 = forms.CharField(
        label='password', 
        required=True, 
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'contraseña nueva'
            }
        )
    )