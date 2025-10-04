# REGroup - Cooperativa de Reciclaje RAEE

## 🌍 Descripción

REGroup es una plataforma web Django para una cooperativa de reciclaje de **RAEE (Residuos de Aparatos Eléctricos y Electrónicos)** autosustentable en Santiago del Estero, Argentina. El proyecto participa en el **NASA Space Apps Challenge 2024**, aplicando tecnología espacial a soluciones de reciclaje sustentable.

### 🎯 Características Principales

- ♻️ **Información sobre RAEE**: Educación sobre reciclaje electrónico
- 🤝 **Gestión Cooperativa**: Modelo de trabajo digno y equitativo
- 🚀 **Proyecto NASA**: Integración de IA y sensores IoT
- 📍 **Puntos de Reciclaje**: Localizador de puntos de recolección
- 📊 **Impacto Medible**: Transparencia en métricas ambientales
- 📝 **Blog Ambiental**: Contenido educativo sobre sostenibilidad
- 🗑️ **Tachy**: Mascota guía (tacho azul)

---

## 🛠️ Tecnologías

- **Backend**: Django 5.2.7
- **Frontend**: Bootstrap 5, HTML5, CSS3, JavaScript
- **Base de Datos**: SQLite (desarrollo) / PostgreSQL (producción recomendado)
- **Python**: 3.12+

---

## 📁 Estructura del Proyecto
REGroup-Django/ ├── .venv/                              # Entorno virtual Python ├── regroup_web/                        # Directorio raíz del proyecto Django │   ├── manage.py                       # Script de gestión Django │   ├── db.sqlite3                      # Base de datos SQLite │   │ │   ├── regroup_web/                    # Paquete de configuración principal │   │   ├── init.py │   │   ├── settings.py                 # Configuración del proyecto │   │   ├── urls.py                     # URLs principales │   │   ├── asgi.py                     # Configuración ASGI │   │   └── wsgi.py                     # Configuración WSGI │   │ │   ├── core/                           # App principal (home, base templates) │   │   ├── migrations/ │   │   ├── templates/ │   │   │   └── core/ │   │   │       ├── base.html           # Template base con navbar/footer │   │   │       └── index.html          # Página de inicio │   │   ├── init.py │   │   ├── admin.py │   │   ├── apps.py │   │   ├── models.py │   │   ├── tests.py │   │   ├── urls.py │   │   └── views.py │   │ │   ├── raee_info/                      # App información sobre RAEE │   │   ├── migrations/ │   │   ├── templates/ │   │   │   └── raee_info/ │   │   │       ├── index.html │   │   │       ├── categoria_detail.html │   │   │       └── materiales_list.html │   │   ├── init.py │   │   ├── admin.py │   │   ├── apps.py │   │   ├── models.py                   # CategoriaRAEE, MaterialRecuperable, InfoRAEE │   │   ├── tests.py │   │   ├── urls.py │   │   └── views.py │   │ │   ├── cooperativa/                    # App gestión cooperativa │   │   ├── migrations/ │   │   ├── templates/ │   │   │   └── cooperativa/ │   │   │       ├── index.html │   │   │       ├── miembros_list.html │   │   │       ├── miembro_detail.html │   │   │       ├── proyectos_list.html │   │   │       ├── proyecto_detail.html │   │   │       ├── impacto.html │   │   │       └── unirse.html │   │   ├── init.py │   │   ├── admin.py │   │   ├── apps.py │   │   ├── models.py                   # Miembro, Proyecto, ImpactoAmbiental │   │   ├── tests.py │   │   ├── urls.py │   │   └── views.py │   │ │   ├── nasa_project/                   # App proyecto NASA │   │   ├── migrations/ │   │   ├── templates/ │   │   │   └── nasa_project/ │   │   │       ├── index.html │   │   │       ├── challenge_detail.html │   │   │       ├── innovaciones_list.html │   │   │       └── timeline.html │   │   ├── init.py │   │   ├── admin.py │   │   ├── apps.py │   │   ├── models.py                   # NASAChallenge, Hito, Innovacion │   │   ├── tests.py │   │   ├── urls.py │   │   └── views.py │   │ │   ├── puntos_reciclaje/               # App puntos de recolección │   │   ├── migrations/ │   │   ├── templates/ │   │   │   └── puntos_reciclaje/ │   │   │       ├── index.html │   │   │       ├── mapa.html │   │   │       ├── punto_detail.html │   │   │       └── solicitar_recoleccion.html │   │   ├── init.py │   │   ├── admin.py │   │   ├── apps.py │   │   ├── models.py                   # PuntoReciclaje, Recoleccion │   │   ├── tests.py │   │   ├── urls.py │   │   └── views.py │   │ │   ├── blog/                           # App blog educativo │   │   ├── migrations/ │   │   ├── templates/ │   │   │   └── blog/ │   │   │       ├── index.html │   │   │       ├── post_detail.html │   │   │       └── categoria_posts.html │   │   ├── init.py │   │   ├── admin.py │   │   ├── apps.py │   │   ├── models.py                   # Categoria, Post, Comentario │   │   ├── tests.py │   │   ├── urls.py │   │   └── views.py │   │ │   ├── static/                         # Archivos estáticos globales │   │   ├── css/ │   │   ├── js/ │   │   └── img/ │   │ │   ├── staticfiles/                    # Archivos estáticos recolectados (producción) │   │ │   └── media/                          # Archivos subidos por usuarios │       ├── raee/ │       ├── miembros/ │       ├── proyectos/ │       ├── innovaciones/ │       └── blog/ │ ├── populate_db.py                      # Script para poblar base de datos ├── requirements.txt                    # Dependencias Python └── README.md                           # Este archivo
---

## 📦 Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/tu-usuario/REGroup-Django.git
cd REGroup-Django
2. Crear entorno virtual
python -m venv .venv
source .venv/bin/activate  # En Linux/Mac
# o
.venv\Scripts\activate     # En Windows
3. Instalar dependencias
pip install -r requirements.txt
4. Configurar base de datos
cd regroup_web
python manage.py makemigrations
python manage.py migrate
5. Poblar base de datos (opcional pero recomendado)
python populate_db.py
Este script crea:
Usuario admin (admin/admin123)
Categorías RAEE y materiales
Miembros fundadores
Proyectos activos
Datos de impacto ambiental
Challenge NASA con hitos
Puntos de reciclaje
Posts del blog
6. Crear superusuario (si no usaste populate_db.py)
python manage.py createsuperuser
7. Ejecutar servidor de desarrollo
python manage.py runserver
Accede a: http://127.0.0.1:8000/
🔑 Credenciales por Defecto
Después de ejecutar populate_db.py:
Usuario: admin
Contraseña: admin123
Admin panel: http://127.0.0.1:8000/admin/
🌐 Rutas Principales
Ruta
Descripción
/
Página de inicio
/admin/
Panel de administración Django
/raee/
Información sobre RAEE
/cooperativa/
Información de la cooperativa
/cooperativa/impacto/
Métricas de impacto ambiental
/cooperativa/unirse/
Formulario de membresía
/nasa/
Proyecto NASA Space Apps
/puntos/
Puntos de reciclaje
/blog/
Blog educativo
📊 Modelos de Datos
raee_info
CategoriaRAEE: Categorías de residuos (Informática, Telefonía, etc.)
MaterialRecuperable: Materiales que se recuperan (Oro, Cobre, Plata, etc.)
InfoRAEE: Información educativa sobre RAEE
cooperativa
Miembro: Miembros de la cooperativa con roles
Proyecto: Proyectos en ejecución
ImpactoAmbiental: Métricas mensuales de impacto
nasa_project
NASAChallenge: Información del proyecto NASA
Hito: Hitos del proyecto
Innovacion: Innovaciones tecnológicas
puntos_reciclaje
PuntoReciclaje: Puntos de recolección con geolocalización
Recoleccion: Registro de recolecciones realizadas
blog
Categoria: Categorías del blog
Post: Artículos del blog
Comentario: Comentarios en posts
🎨 Características de Diseño
Diseño responsive con Bootstrap 5
Tema moderno con gradientes
Iconos Bootstrap Icons
Tachy flotante (mascota)
Animaciones CSS
Navbar sticky
Footer informativo
🚀 Despliegue en Producción
Variables de Entorno
SECRET_KEY=tu-secret-key-super-segura
DEBUG=False
ALLOWED_HOSTS=tudominio.com,www.tudominio.com
DATABASE_URL=postgresql://user:pass@localhost/dbname
Recolectar archivos estáticos
python manage.py collectstatic
Configurar base de datos PostgreSQL
Edita settings.py:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'regroup_db',
        'USER': 'regroup_user',
        'PASSWORD': 'tu_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
🧪 Testing
python manage.py test
📝 Comandos Útiles
# Crear nueva app
python manage.py startapp nombre_app

# Hacer migraciones
python manage.py makemigrations
python manage.py migrate

# Crear superusuario
python manage.py createsuperuser

# Shell interactivo
python manage.py shell

# Recolectar estáticos
python manage.py collectstatic
