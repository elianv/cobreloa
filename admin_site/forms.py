from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class LoginForm(forms.ModelForm):
    

    class Meta:
        model = User
        fields = ['username', 'password', 'email']
        labels = {'username': 'Nombre usuario', 'email': 'Email'}
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Usuario'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Contraseña'})
        }

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user or not user.is_active:
            raise forms.ValidationError("Nombre de usuario/contraseña incorrecto.")
        return self.cleaned_data

    def login(self, request):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        return user        