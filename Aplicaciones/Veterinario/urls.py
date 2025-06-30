from django.urls import path
from . import views

urlpatterns = [
    path('Veterinario', views.Inicio_Veterinarios),
    path('NuevoVeterinario', views.NuevoVeterinario),
    path('GuardarVeterinario', views.GuardarVeterinario),
    path('EditarVeterinario/<int:id>', views.EditarVeterinario),
    path('ProcesarVeterinario', views.ProcesarVeterinario),
    path('EliminarVeterinario/<int:id>', views.EliminarVeterinario),
]
