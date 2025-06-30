from django.db import models


class Vacuna(models.Model):
    nombre = models.CharField(max_length=100)
    fabricante = models.CharField(max_length=100)
    dosis = models.DecimalField(max_digits=5, decimal_places=2)
    edad_aplicacion = models.PositiveIntegerField()  # en semanas
    vigencia = models.PositiveIntegerField()  # en meses
    tipo = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
