# Proyecto 8 - Sistema de Gestión de Eventos y Reservas

Este proyecto es un sistema backend desarrollado con Django y Django REST Framework para gestionar eventos, reservas y reportes de ocupación.

## Instalación

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/Donko-hh/proyecto-eventos.git
   cd proyecto-eventos/backend
   ```

2. Crear entorno virtual e instalar dependencias:
    python -m venv venv
    venv\Scripts\activate   # Windows
    pip install -r requirements.txt

3. Configurar base de datos MySQL en core/settings.py.

4. Ejecutar migraciones:
    python manage.py migrate

5. Crear superusuario:
    python manage.py createsuperuser

6. Levantar el servidor:
    python manage.py runserver

## Endpoints principales
- /api/eventos/ → CRUD de eventos

- /api/reservas/ → CRUD de reservas

- /api/reportes/ocupacion/ → reporte de ocupación

- /swagger/ → documentación interactiva de la API

- /admin/ → panel de administración

## Tecnologías
- Django 5.2
- Django REST Framework
- drf-yasg (Swagger)
- MySQL + PyMySQL