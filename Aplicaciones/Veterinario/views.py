from django.shortcuts import render, redirect
from .models import Veterinario
from django.contrib import messages

def Inicio_Veterinarios(request):
    veterinarios = Veterinario.objects.all()
    return render(request, "inicioVeterinarios.html", {"veterinarios": veterinarios})

def NuevoVeterinario(request):
    return render(request, "nuevoVeterinario.html")

def GuardarVeterinario(request):
    if request.method == 'POST':
        Veterinario.objects.create(
            nombre=request.POST.get('nombre'),
            especialidad=request.POST.get('especialidad'),
            licencia=request.POST.get('licencia'),
            experiencia=request.POST.get('experiencia'),
            turno=request.POST.get('turno'),
            contacto=request.POST.get('contacto')
        )
        messages.success(request, "Veterinario guardado exitosamente.")
    return redirect('/Veterinario')

def EliminarVeterinario(request, id):
    veterinario = Veterinario.objects.get(id=id)
    veterinario.delete()
    messages.success(request, "Veterinario eliminado exitosamente.")
    return redirect('/Veterinario')

def EditarVeterinario(request, id):
    veterinario = Veterinario.objects.get(id=id)
    return render(request, "editarVeterinario.html", {"veterinario": veterinario})

def ProcesarVeterinario(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        nombre = request.POST.get('nombre')
        especialidad = request.POST.get('especialidad')
        licencia = request.POST.get('licencia')
        experiencia = request.POST.get('experiencia')
        turno = request.POST.get('turno')
        contacto = request.POST.get('contacto')

        veterinario = Veterinario.objects.get(id=id)
        veterinario.nombre = nombre
        veterinario.especialidad = especialidad
        veterinario.licencia = licencia
        veterinario.experiencia = experiencia
        veterinario.turno = turno
        veterinario.contacto = contacto
        veterinario.save()

        messages.success(request, "Veterinario actualizado exitosamente.")
    return redirect('/Veterinario')
