
from django.urls import path, include

from .views import *

from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', HomeView.as_view(), name="home"),

    #LISTADOS
    path('propiedad/', PropiedadList.as_view(), name="propiedad"),
    path('operacion/', OperacionList.as_view(), name="operacion"),
    path('estado/', EstadoList.as_view(), name="estado"),
    path('ciudad/', CiudadList.as_view(), name="ciudad"),

    #CREAR / MODIFICAR
    path('propiedad-crear/', PropiedadCreate.as_view(), name="propiedad-create"),
    path('propiedad-modificar/<int:pk>/', PropiedadUpdate.as_view(), name="propiedad-update"),
    path('ciudad-crear/', CiudadCreate.as_view(), name="ciudad-create"),


    #ELIMINAR
    path('ciudad-eliminar/<int:pk>/', CiudadDelete.as_view(), name="ciudad-eliminar"),

    #LOGIN / LOGOUT
    path('login/',  MyLoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(next_page="login"), name="logout"),
]