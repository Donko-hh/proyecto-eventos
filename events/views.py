from rest_framework import viewsets, permissions
from django_filters.rest_framework import DjangoFilterBackend
from .models import Evento
from .serializers import EventoSerializer

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_authenticated and getattr(request.user, 'role', 'user') == 'admin'

class EventoViewSet(viewsets.ModelViewSet):
    queryset = Evento.objects.all().order_by('fecha', 'hora')
    serializer_class = EventoSerializer
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['estado', 'fecha', 'nombre']

    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.user.is_authenticated and getattr(self.request.user, 'role', 'user') == 'admin':
            return qs
        return qs.filter(estado='activo')