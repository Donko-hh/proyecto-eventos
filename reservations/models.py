from django.db import models
from django.core.exceptions import ValidationError
from events.models import Evento

class Reserva(models.Model):
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name="reservas")
    nombre_cliente = models.CharField(max_length=100)
    correo_cliente = models.EmailField()
    cantidad = models.PositiveIntegerField()
    fecha_reserva = models.DateTimeField(auto_now_add=True)
    asistio = models.BooleanField(default=False)

class Reserva(models.Model):
    evento = models.ForeignKey("events.Evento", on_delete=models.CASCADE, related_name="reservas")
    nombre_cliente = models.CharField(max_length=100)
    correo_cliente = models.EmailField()
    cantidad = models.PositiveIntegerField()
    fecha_reserva = models.DateTimeField(auto_now_add=True)
    asistio = models.BooleanField(default=False)

    def clean(self):
        if self.cantidad <= 0:
            raise ValidationError("La cantidad debe ser mayor a 0.")

        if self.evento.estado != 'activo':
            raise ValidationError("No se puede reservar en un evento inactivo.")

        reservado = sum(r.cantidad for r in self.evento.reservas.exclude(pk=self.pk))
        disponible = self.evento.capacidad - reservado

        if disponible <= 0:
            raise ValidationError("Este evento ya no tiene cupos disponibles.")
        if self.cantidad > disponible:
            raise ValidationError(f"Solo quedan {disponible} cupos disponibles para este evento.")

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)
    asistio = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.nombre_cliente} - {self.evento.nombre}"