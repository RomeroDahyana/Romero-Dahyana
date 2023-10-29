
from typing import Any
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib import messages

# Create your views here.
# Modelos
from .models import Ciudad, Operacion, Propiedad, Estado
from .forms import PropiedadForm, CiudadForm


# CBV

from django.views.generic import TemplateView
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.contrib.auth.views import LoginView

class HomeView(TemplateView):
    template_name = "app/home.html"

class CiudadList(ListView):
    model = Ciudad

class CiudadCreate(CreateView):
    model = Ciudad
    form_class = CiudadForm
    success_url = reverse_lazy('propiedad')

class CiudadDelete(DeleteView):
    model = Ciudad
    success_url = reverse_lazy('propiedad')
  
    
class OperacionList(ListView):
    model = Operacion



class EstadoList(ListView):
    model = Estado



class PropiedadList(ListView):
    model = Propiedad


class PropiedadCreate (CreateView):
    model = Propiedad 
    form_class = PropiedadForm
    success_url = reverse_lazy('propiedad')

class PropiedadUpdate (UpdateView):
    model = Propiedad 
    form_class = PropiedadForm
    template_name = 'propiedad-update.html'
    success_url = reverse_lazy('propiedad')
    
'''
class EliminarPropiedad(DeleteView):   
    model = Propiedad
    success_url = reverse_lazy('propiedad')
'''

class MyLoginView(LoginView):
    redirect_authenticated_user = True
    def get_success_url(self):
        return reverse_lazy('propiedad')
    
    def form_invalid(self, form):
        messages.error(self.requests, "Por favor, revise su login. Usuario o contraseña incorrectos")
        return self.render_to_response(self.get_context_data(form=form))
