from django.urls import path
from . import views

urlpatterns = [
    path('', views.Inicio_Mascotas),
    path('NuevaMascota', views.NuevaMascota),
    path('GuardarMascota', views.GuardarMascota),
    path('EditarMascota/<int:id>', views.EditarMascota),
    path('ProcesarMascota', views.ProcesarMascota),
    path('EliminarMascota/<int:id>', views.EliminarMascota),
]
