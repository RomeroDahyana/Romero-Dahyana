
from typing import Any
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib import messages

# Create your views here.
# Modelos
from .models import Ciudad, Operacion, Propiedad, Estado
from .forms import PropiedadForm, CiudadForm, OperacionForm, EstadoForm


# CBV

from django.views.generic import TemplateView
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.contrib.auth.views import LoginView

class HomeView(TemplateView):
    template_name = "app/home.html"

#CIUDAD
class CiudadList(ListView):
    model = Ciudad

class CiudadCreate(CreateView):
    model = Ciudad
    form_class = CiudadForm
    success_url = reverse_lazy('propiedad')

class CiudadUpdate(UpdateView):
    model = Ciudad
    form_class = CiudadForm
    
    template_name_suffix = "_update_form" 

    def get_success_url(self):
        return reverse_lazy('ciudad-actualizar', args=[self.object.id])

class CiudadDelete(DeleteView):
    model = Ciudad
    success_url = reverse_lazy('propiedad')
  
#OPERACION    
class OperacionList(ListView):
    model = Operacion

class OperacionCreate(CreateView):
    model = Operacion
    form_class = OperacionForm
    success_url = reverse_lazy('operacion')

class OperacionUpdate(UpdateView):
    model = Operacion
    form_class = OperacionForm
    
    template_name_suffix = "_update_form" 

    success_url = reverse_lazy('operacion')

class OperacionDelete(DeleteView):
    model = Operacion
    success_url = reverse_lazy('operacion')


#ESTADO
class EstadoList(ListView):
    model = Estado

class EstadoCreate(CreateView):
    model = Estado
    form_class = EstadoForm
    success_url = reverse_lazy('estado')

class EstadoUpdate(UpdateView):
    model = Estado
    form_class = EstadoForm
    
    template_name_suffix = "_update_form" 
    success_url = reverse_lazy('estado')

    
class EstadoDelete(DeleteView):
    model = Estado
    success_url = reverse_lazy('estado')



#PROPIEDADES
class PropiedadList(ListView):
    model = Propiedad


class PropiedadCreate (CreateView):
    model = Propiedad 
    form_class = PropiedadForm
    success_url = reverse_lazy('propiedad')

class PropiedadUpdate(UpdateView):
    model = Propiedad
    form_class = PropiedadForm
    
    template_name_suffix = "_update_form" 
    success_url = reverse_lazy('propiedad')
    

class PropiedadDelete(DeleteView):   
    model = Propiedad
    success_url = reverse_lazy('propiedad')

#LOGIN

class MyLoginView(LoginView):
    redirect_authenticated_user = True
    def get_success_url(self):
        return reverse_lazy('propiedad')
    
    def form_invalid(self, form):
        messages.error(self.requests, "Por favor, revise su login. Usuario o contraseña incorrectos")
        return self.render_to_response(self.get_context_data(form=form))

#ACERCA DE MI
def acercademi(request):
    context = {
        'titulo': 'Acerca de Mí',
        'contenido': 'Esta es la página de acerca de mí. Aquí puedes agregar información personal.',
    }
    return render(request, 'app/acerca.html', context)