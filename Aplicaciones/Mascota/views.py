from django.shortcuts import render, redirect
from .models import Mascota
from django.contrib import messages

def Inicio_Mascotas(request):
    mascotas = Mascota.objects.all()
    return render(request, "inicioMascotas.html", {"mascotas": mascotas})

def NuevaMascota(request):
    return render(request, "nuevaMascota.html")

def GuardarMascota(request):
    if request.method == 'POST':
        Mascota.objects.create(
            nombre=request.POST.get('nombre'),
            especie=request.POST.get('especie'),
            raza=request.POST.get('raza'),
            edad=request.POST.get('edad'),
            peso=request.POST.get('peso'),
            propietario=request.POST.get('propietario')
        )
        messages.success(request, "Mascota guardada exitosamente.")
    return redirect('/')

def EliminarMascota(request, id):
    mascota = Mascota.objects.get(id=id)
    mascota.delete()
    messages.success(request, "Mascota eliminada exitosamente.")
    return redirect('/')

def EditarMascota(request, id):
    mascota = Mascota.objects.get(id=id)
    peso = str(mascota.peso).replace(',', '.')
    return render(request, "editarMascota.html", {"mascota": mascota,'peso': peso})

def ProcesarMascota(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        nombre = request.POST.get('nombre')
        especie = request.POST.get('especie')
        raza = request.POST.get('raza')
        edad = request.POST.get('edad')
        peso = request.POST.get('peso')
        propietario = request.POST.get('propietario')

        mascota = Mascota.objects.get(id=id)
        mascota.nombre = nombre
        mascota.especie = especie
        mascota.raza = raza
        mascota.edad = edad
        mascota.peso = peso
        mascota.propietario = propietario
        mascota.save()

        messages.success(request, "Mascota actualizada exitosamente.")
    return redirect('/')

