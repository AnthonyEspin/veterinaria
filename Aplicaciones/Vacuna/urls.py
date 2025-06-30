from django.urls import path
from . import views

urlpatterns = [
    path('Vacuna', views.Inicio_Vacunas),
    path('NuevaVacuna', views.NuevaVacuna),
    path('GuardarVacuna', views.GuardarVacuna),
    path('EditarVacuna/<int:id>', views.EditarVacuna),
    path('ProcesarVacuna', views.ProcesarVacuna),
    path('EliminarVacuna/<int:id>', views.EliminarVacuna),
]
