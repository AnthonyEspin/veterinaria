from django.shortcuts import render, redirect
from .models import Vacuna
from django.contrib import messages

def Inicio_Vacunas(request):
    vacunas = Vacuna.objects.all()
    return render(request, "inicioVacunas.html", {"vacunas": vacunas})

def NuevaVacuna(request):
    return render(request, "nuevaVacuna.html")

def GuardarVacuna(request):
    if request.method == 'POST':
        Vacuna.objects.create(
            nombre=request.POST.get('nombre'),
            fabricante=request.POST.get('fabricante'),
            dosis=request.POST.get('dosis'),
            edad_aplicacion=request.POST.get('edad_aplicacion'),
            vigencia=request.POST.get('vigencia'),
            tipo=request.POST.get('tipo')
        )
        messages.success(request, "Vacuna guardada exitosamente.")
    return redirect('/Vacuna')

def EliminarVacuna(request, id):
    vacuna = Vacuna.objects.get(id=id)
    vacuna.delete()
    messages.success(request, "Vacuna eliminada exitosamente.")
    return redirect('/Vacuna')

def EditarVacuna(request, id):
    vacuna = Vacuna.objects.get(id=id)
    dosis = str(vacuna.dosis).replace(',', '.')
    return render(request, "editarVacuna.html", {"vacuna": vacuna, 'dosis': dosis})

def ProcesarVacuna(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        nombre = request.POST.get('nombre')
        fabricante = request.POST.get('fabricante')
        dosis = request.POST.get('dosis')
        edad_aplicacion = request.POST.get('edad_aplicacion')
        vigencia = request.POST.get('vigencia')
        tipo = request.POST.get('tipo')

        vacuna = Vacuna.objects.get(id=id)
        vacuna.nombre = nombre
        vacuna.fabricante = fabricante
        vacuna.dosis = dosis
        vacuna.edad_aplicacion = edad_aplicacion
        vacuna.vigencia = vigencia
        vacuna.tipo = tipo
        vacuna.save()

        messages.success(request, "Vacuna actualizada exitosamente.")
    return redirect('/Vacuna')
