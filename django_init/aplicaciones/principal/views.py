from django import forms
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Persona
from .forms import Personaform

def inicio(request):
    personas = Persona.objects.all()    
    contexto={
        'personas':personas
    }
    return render(request,'index.html',contexto)

def crear(request):
    if request.method == 'GET':
        form = Personaform()        
    else:
        form = Personaform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index') 
                
    return render(request,'crear.html', {'form':form})

def editar (request,id):
    persona = Persona.objects.get(id = id)
    if request.method =='GET':
        form= Personaform(instance= persona)        
    else:
        form = Personaform(request.POST, instance=persona)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render (request,'crear.html',{'form':form})
def eliminar (request,id):
    persona = Persona.objects.get(id =id)
    persona.delete()
    return redirect('index')
