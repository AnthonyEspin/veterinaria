from django.db import models

class Veterinario(models.Model):
    nombre = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)
    licencia = models.CharField(max_length=50)
    experiencia = models.PositiveIntegerField()  # años
    turno = models.CharField(max_length=50)
    contacto = models.CharField(max_length=15)

    def __str__(self):
        return self.nombre
