from django.db import models
from django.core.exceptions import ValidationError


class Evento(models.Model):
    ESTADO_CHOICES = [
        ('activo', 'Activo'),
        ('inactivo', 'Inactivo'),
    ]

    nombre = models.CharField(max_length=100)
    fecha = models.DateField()
    hora = models.TimeField()
    duracion = models.IntegerField(help_text="Duración en minutos")
    capacidad = models.IntegerField()
    descripcion = models.TextField()
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='activo')

    def espacio_disponible(self):
        total_reservado = sum(reserva.cantidad for reserva in self.reservas.all())
        return self.capacidad - total_reservado

    def __str__(self):
        return self.nombre
    
    def clean(self):
        if self.capacidad < 0:
            raise ValidationError('La capacidad no puede ser negativa.')
