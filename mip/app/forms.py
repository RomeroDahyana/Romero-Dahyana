from django import forms
from .models import Propiedad, Ciudad
from django.core.exceptions import ValidationError


class PropiedadForm (forms.ModelForm):
    class Meta:    
        model = Propiedad
        fields = ['name', 'description', 'estado', 'ciudad',  'operacion', 'image', 'costo']


        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Propiedad'}),
            'description':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Descripción'}),
            'estado': forms.Select(attrs={'class':'form-control', 'placeholder':'Estado'}),
            'ciudad': forms.SelectMultiple(attrs={'class':'form-control', 'placeholder':'Ciudad'}),
            'provincia': forms.Select(attrs={'class':'form-control', 'placeholder':'Provincia'}),
            'costo': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Precio'}),
        } 
    
        labels = {
            'name': "",
            'description': ""
            }
        
class CiudadForm (forms.ModelForm):
    class Meta:
        model = Ciudad
        fields = ['name']
        exclude = ['created', 'updated']

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ciudad'}),
        }