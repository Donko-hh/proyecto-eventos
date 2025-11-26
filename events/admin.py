from django.contrib import admin
from .models import Evento

# Register your models here.

@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha', 'hora', 'capacidad', 'estado')
    search_fields = ('nombre', 'descripcion')
    list_filter = ('estado', 'fecha')