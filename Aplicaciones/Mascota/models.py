from django.db import models


class Mascota(models.Model):
    nombre = models.CharField(max_length=100)
    especie = models.CharField(max_length=50)
    raza = models.CharField(max_length=50)
    edad = models.PositiveIntegerField()
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    propietario = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
