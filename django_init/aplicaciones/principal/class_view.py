from django.shortcuts import render ,redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView,ListView,UpdateView
from .forms import Personaform
from .models import Persona

class PersonaList(ListView):
    model = Persona
    template_name= 'index.html'

class PersonaCreate(CreateView):
    model = Persona
    form_class = Personaform
    template_name = 'crear.html'
    success_url= reverse_lazy('index')

class PersonaEditar(UpdateView):
    model = Persona
    form_class = Personaform
    template_name = 'crear.html'
    success_url= reverse_lazy('index')

class PersonaEliminar(DeleteView):
    model = Persona
    template_name = 'verificacion.html'
    success_url= reverse_lazy('index')
    
