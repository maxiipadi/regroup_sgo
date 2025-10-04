## 📁 Estructura del Proyecto

```
REGroup-Django/
│
├── .venv/                                      # Entorno virtual Python
│
├── regroup_web/                                # Directorio raíz Django
│   │
│   ├── manage.py                               # Script de gestión Django
│   ├── db.sqlite3                              # Base de datos SQLite
│   │
│   ├── regroup_web/                            # Configuración principal
│   │   ├── __init__.py
│   │   ├── settings.py                         # Configuración del proyecto
│   │   ├── urls.py                             # URLs principales
│   │   ├── asgi.py                             # Configuración ASGI
│   │   └── wsgi.py                             # Configuración WSGI
│   │
│   ├── core/                                   # App principal
│   │   ├── migrations/
│   │   ├── templates/
│   │   │   └── core/
│   │   │       ├── base.html                   # Template base
│   │   │       └── index.html                  # Página inicio
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   │
│   ├── raee_info/                              # Información RAEE
│   │   ├── migrations/
│   │   ├── templates/
│   │   │   └── raee_info/
│   │   │       ├── index.html
│   │   │       ├── categoria_detail.html
│   │   │       └── materiales_list.html
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py                           # CategoriaRAEE, etc.
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   │
│   ├── cooperativa/                            # Gestión cooperativa
│   │   ├── migrations/
│   │   ├── templates/
│   │   │   └── cooperativa/
│   │   │       ├── index.html
│   │   │       ├── miembros_list.html
│   │   │       ├── miembro_detail.html
│   │   │       ├── proyectos_list.html
│   │   │       ├── proyecto_detail.html
│   │   │       ├── impacto.html
│   │   │       └── unirse.html
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py                           # Miembro, Proyecto, etc.
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   │
│   ├── nasa_project/                           # Proyecto NASA
│   │   ├── migrations/
│   │   ├── templates/
│   │   │   └── nasa_project/
│   │   │       ├── index.html
│   │   │       ├── challenge_detail.html
│   │   │       ├── innovaciones_list.html
│   │   │       └── timeline.html
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py                           # NASAChallenge, Hito, etc.
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   │
│   ├── puntos_reciclaje/                       # Puntos de recolección
│   │   ├── migrations/
│   │   ├── templates/
│   │   │   └── puntos_reciclaje/
│   │   │       ├── index.html
│   │   │       ├── mapa.html
│   │   │       ├── punto_detail.html
│   │   │       └── solicitar_recoleccion.html
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py                           # PuntoReciclaje, etc.
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   │
│   ├── blog/                                   # Blog educativo
│   │   ├── migrations/
│   │   ├── templates/
│   │   │   └── blog/
│   │   │       ├── index.html
│   │   │       ├── post_detail.html
│   │   │       └── categoria_posts.html
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py                           # Categoria, Post, etc.
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   │
│   ├── static/                                 # Archivos estáticos
│   │   ├── css/
│   │   ├── js/
│   │   └── img/
│   │
│   ├── staticfiles/                            # Estáticos recolectados
│   │
│   └── media/                                  # Uploads
│       ├── raee/
│       ├── miembros/
│       ├── proyectos/
│       ├── innovaciones/
│       └── blog/
│
├── populate_db.py                              # Script de datos
├── requirements.txt                            # Dependencias
└── README.md                                   # Documentación
```
