
from django.urls import path, include

from .views import *
from . import views

from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', HomeView.as_view(), name="home"),

    #LISTADOS
    path('propiedad/', PropiedadList.as_view(), name="propiedad"),
    path('operacion/', OperacionList.as_view(), name="operacion"),
    path('estado/', EstadoList.as_view(), name="estado"),
    path('ciudad/', CiudadList.as_view(), name="ciudad"),

    #CREAR 
    path('ciudad-crear/', CiudadCreate.as_view(), name="ciudad-create"),
    path('operacion-crear/', OperacionCreate.as_view(), name="operacion-create"),
    path('estado-crear/', EstadoCreate.as_view(), name="estado-create"),
    path('propiedad-crear/', PropiedadCreate.as_view(), name="propiedad-create"),


    #MODIFICAR
    path('propiedad-modificar/<int:pk>/', PropiedadUpdate.as_view(), name="propiedad-actualizar"),
    path('ciudad-actualizar/<int:pk>/', CiudadUpdate.as_view(), name="ciudad-actualizar"),
    path('estado-actualizar/<int:pk>/', EstadoUpdate.as_view(), name="estado-actualizar"),
    path('operacion-actualizar/<int:pk>/', OperacionUpdate.as_view(), name="operacion-actualizar"),
    

    #ELIMINAR
    path('propiedad-eliminar/<int:pk>/', PropiedadDelete.as_view(), name="propiedad-eliminar"),
    path('ciudad-eliminar/<int:pk>/', CiudadDelete.as_view(), name="ciudad-eliminar"),
    path('estado-eliminar/<int:pk>/', EstadoDelete.as_view(), name="estado-eliminar"),
    path('operacion-eliminar/<int:pk>/', OperacionDelete.as_view(), name="operacion-eliminar"),

    #LOGIN / LOGOUT
    path('login/',  MyLoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(next_page="login"), name="logout"),

    #ACERCA DE MI
    path('app/acerca.html', views.acercademi, name='acercademi'),
]