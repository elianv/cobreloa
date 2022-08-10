from django import forms
from socios.models import Socio

class SocioForm(forms.ModelForm):
    class Meta:
        model = Socio
        fields = ['rut', 'dv', 'correo', 'nombres', 'apellidos', 'direccion', 'telefono', 'fecha_nacimiento', 'ocupacion']
        labels = {
            'rut': 'RUT',
            'dv': 'DV',
            'correo': 'E-mail',
            'nombres': 'Nombres',
            'apellidos': 'Apellidos',
            'direccion': 'Dirección completa',
            'telefono': 'Teléfono',
            #'foto': 'Foto carnet',
            'fecha_nacimiento': 'Fecha nacimiento',
            'ocupacion': 'Ocupación'
        }
        
        widgets = {
            'rut': forms.TextInput(attrs={'class':'form-control', 'placeholder': '11222333-K'}),
            #'dv': forms.CharField(),
            'correo': forms.EmailInput(attrs={'class': 'form-control'}),
            'nombres': forms.TextInput(attrs={'class': 'form-control'}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '911112233'}),
            #'foto': forms.ImageField(),
            'fecha_nacimiento': forms.TextInput(attrs={'class': 'form-control datetimepicker-input', 'data-target':"#reservationdate", 'placeholder': 'dd/mm/aaaa'}),
            'ocupacion': forms.Select(attrs={'class': 'form-control select2'})
        }
        
        
