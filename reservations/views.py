from rest_framework import viewsets, permissions, status
from .models import Reserva
from .serializers import ReservaSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from django.core.exceptions import ValidationError

class IsAdminOrOwnerCreate(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return request.user.is_authenticated
        return request.user.is_authenticated

class ReservaViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.select_related('evento').all().order_by('-fecha_reserva')
    serializer_class = ReservaSerializer
    permission_classes = [IsAdminOrOwnerCreate]

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated and getattr(user, 'role', 'user') == 'admin':
            return self.queryset
        return self.queryset

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as e:
            return Response(
                {"detalle": e.message_dict.get('__all__', ["Error de validación"])},
                status=status.HTTP_400_BAD_REQUEST
            )

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAdminUser])
    def marcar_asistencia(self, request, pk=None):
        reserva = self.get_object()
        reserva.asistio = True
        reserva.save()
        return Response({'status': 'asistencia marcada'})
