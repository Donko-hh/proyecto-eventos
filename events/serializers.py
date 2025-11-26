from rest_framework import serializers
from .models import Evento

class EventoSerializer(serializers.ModelSerializer):
    disponible = serializers.SerializerMethodField()

    class Meta:
        model = Evento
        fields = '__all__'

    def get_disponible(self, obj):
        reservado = sum(r.cantidad for r in obj.reservas.all())
        return obj.capacidad - reservado
