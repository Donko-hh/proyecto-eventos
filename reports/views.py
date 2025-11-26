from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from events.models import Evento
from reservations.models import Reserva
from django.db.models import Sum

# Create your views here.

class OcupacionReportView(APIView):
    permission_classes = [permissions.IsAdminUser]

    def get(self, request):
        data = []
        eventos = Evento.objects.all()
        for e in eventos:
            reservado = e.reservas.aggregate(total=Sum('cantidad'))['total'] or 0
            data.append({
                'evento_id': e.id,
                'nombre': e.nombre,
                'capacidad': e.capacidad,
                'reservado': reservado,
                'disponible': e.capacidad - reservado,
            })
        return Response(data)