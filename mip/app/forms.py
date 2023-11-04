from django import forms
from .models import Propiedad, Ciudad, Operacion, Estado
from django.core.exceptions import ValidationError


class PropiedadForm (forms.ModelForm):

    class Meta:    
        model = Propiedad
        fields = ['name', 'description', 'estado', 'ciudad',  'operacion', 'image', 'costo']

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Propiedad'}),
            'description':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Descripción'}),
            'estado': forms.Select(attrs={'class':'form-control', 'placeholder':'Estado'}),
            'ciudad': forms.Select(attrs={'class':'form-control', 'placeholder':'Ciudad'}),
            'operacion': forms.Select(attrs={'class':'form-control', 'placeholder':'Operación'}),
            'costo': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Precio'}),
            
        
        } 
    
        labels = {
            'name': "",
            'description': ""
            }
        
class CiudadForm (forms.ModelForm):
    class Meta:
        model = Ciudad
        fields = ['name', 'codigo_postal']
        exclude = ['created', 'updated']

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ciudad'}),
            'codigo_postal': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Código postal'}),
        }

class OperacionForm (forms.ModelForm):
    class Meta:
        model = Operacion
        fields = ['name']
        exclude = ['created', 'updated']

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Operación'}),
        }

class EstadoForm (forms.ModelForm):
    class Meta:
        model = Estado
        fields = ['name']
        exclude = ['created', 'updated']

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Estado'}),
        }