from django.http import HttpResponse

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
                <p>Este es el prototipo del proyecto 8.</p>
                <a href="/api/eventos/">Ver Eventos</a>
                <a href="/api/reservas/">Ver Reservas</a>
                <a href="/admin/">Administración</a>
            </body>
        </html>
    """)
