from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.ModelForm):
    

    class Meta:
        model = User
        fields = ['username', 'password', 'email']
        labels = {'username': 'Nombre usuario', 'email': 'Email'}
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Usuario'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Contraseña'})
        }