from django.contrib import admin
from .models import Reserva

# Register your models here.

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('evento', 'nombre_cliente', 'correo_cliente', 'cantidad', 'fecha_reserva')
    search_fields = ('nombre_cliente', 'correo_cliente')
    list_filter = ('evento',)