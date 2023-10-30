from django.db import models
from django.contrib import admin
from django.utils.html import format_html

# Create your models here.
   



#CIUDAD
class Ciudad(models.Model):
    name = models.CharField(verbose_name="Ciudad", max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    codigo_postal = models.IntegerField(verbose_name="CodigoPostal",  null=True, blank=True)

    
    class Meta:
        verbose_name = "Ciudad"
        verbose_name_plural = "Ciudades"
    def __str__(self):
        return self.name

#ESTADO
class Estado(models.Model):
    name = models.CharField(verbose_name="Estado", max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    
    class Meta:
        verbose_name = "Estado"
        verbose_name_plural = "Estados"
    def __str__(self):
        return self.name


#OPERACIÓN

class Operacion (models.Model):
    name = models.CharField(verbose_name = "Operación", max_length=50)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Tipo de operación"
        verbose_name_plural = "Tipos de operación"

    def __str__(self):
        return self.name


#PROPIEDADES DISPONIBLES
class Propiedad(models.Model):
    name = models.CharField(verbose_name="Propiedades", max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    description = models.TextField(verbose_name="Descripción de la propiedad") 
    estado = models.ForeignKey(Estado, verbose_name="Estado", on_delete=models.CASCADE)
    ciudad = models.ManyToManyField(Ciudad, verbose_name="Ciudad")
    operacion = models.ForeignKey(Operacion, verbose_name="Tipo de operación", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="alquilerimg", null=True, blank=True, verbose_name="Portada")
    costo = models.DecimalField(verbose_name="Costo", null=False, blank=False, max_digits=10,decimal_places=2)
 


    class Meta:
        verbose_name = "Propiedad disponible"
        verbose_name_plural = "Propiedades disponibles"
    
    def __str__(self):
        return self.name
