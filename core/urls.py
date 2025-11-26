"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from events.views import EventoViewSet
from reservations.views import ReservaViewSet
from authapp.views import UserViewSet
from reports.views import OcupacionReportView
from django.http import HttpResponse

# Swagger imports
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Eventos API",
        default_version='v1',
        description="Documentación de la API de gestión de eventos y reservas",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

def home(request):
    return HttpResponse("""
        <html>
            <head>
                <title>Sistema de Gestión de Eventos</title>
                <style>
                    body { font-family: Arial; background: #f4f4f4; text-align: center; padding: 50px; }
                    h1 { color: #333; }
                    a { display: inline-block; margin: 10px; padding: 10px 20px; background: #007BFF; color: white; text-decoration: none; border-radius: 5px; }
                    a:hover { background: #0056b3; }
                </style>
            </head>
            <body>
                <h1>Bienvenido al Sistema de Gestión de Eventos y Reservas</h1>
                <p>Este es el prototipo del Proyecto 8.</p>
                <a href="/api/eventos/">Ver Eventos</a>
                <a href="/api/reservas/">Ver Reservas</a>
                <a href="/admin/">Administración</a>
            </body>
        </html>
    """)

router = DefaultRouter()
router.register(r'eventos', EventoViewSet)
router.register(r'reservas', ReservaViewSet)
router.register(r'usuarios', UserViewSet)

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/reportes/ocupacion/', OcupacionReportView.as_view(), name='reporte-ocupacion'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
