# REGroup - Cooperativa de Reciclaje RAEE

## 🌍 Descripción

**REGroup** es una plataforma web Django para una cooperativa de reciclaje de **RAEE (Residuos de Aparatos Eléctricos y Electrónicos)** autosustentable en Santiago del Estero, Argentina.  
El proyecto participa en el **NASA Space Apps Challenge 2024**, aplicando tecnología espacial a soluciones de reciclaje sustentable.

---

## 🎯 Características Principales

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

REGroup-Django/ ├── .venv/                             # Entorno virtual Python ├── regroup_web/                       # Directorio raíz del proyecto Django │   ├── manage.py                      # Script de gestión Django │   ├── db.sqlite3                     # Base de datos SQLite │   │ │   ├── regroup_web/                   # Paquete de configuración principal │   │   ├── init.py │   │   ├── settings.py                # Configuración del proyecto │   │   ├── urls.py                    # URLs principales │   │   ├── asgi.py                    # Configuración ASGI │   │   └── wsgi.py                    # Configuración WSGI │   │ │   ├── core/                          # App principal (home, base templates) │   │   ├── migrations/ │   │   ├── templates/core/ │   │   │   ├── base.html              # Template base con navbar/footer │   │   │   └── index.html             # Página de inicio │   │   ├── init.py │   │   ├── admin.py │   │   ├── apps.py │   │   ├── models.py │   │   ├── tests.py │   │   ├── urls.py │   │   └── views.py │   │ │   ├── raee_info/                     # App información sobre RAEE │   │   ├── migrations/ │   │   ├── templates/raee_info/ │   │   │   ├── index.html │   │   │   ├── categoria_detail.html │   │   │   └── materiales_list.html │   │   ├── init.py │   │   ├── admin.py │   │   ├── apps.py │   │   ├── models.py                  # CategoriaRAEE, MaterialRecuperable, InfoRAEE │   │   ├── tests.py │   │   ├── urls.py │   │   └── views.py │   │ │   ├── cooperativa/                   # App gestión cooperativa │   │   ├── migrations/ │   │   ├── templates/cooperativa/ │   │   │   ├── index.html │   │   │   ├── miembros_list.html │   │   │   ├── miembro_detail.html │   │   │   ├── proyectos_list.html │   │   │   ├── proyecto_detail.html │   │   │   ├── impacto.html │   │   │   └── unirse.html │   │   ├── init.py │   │   ├── admin.py │   │   ├── apps.py │   │   ├── models.py                  # Miembro, Proyecto, ImpactoAmbiental │   │   ├── tests.py │   │   ├── urls.py │   │   └── views.py │   │ │   ├── nasa_project/                  # App proyecto NASA │   │   ├── migrations/ │   │   ├── templates/nasa_project/ │   │   │   ├── index.html │   │   │   ├── challenge_detail.html │   │   │   ├── innovaciones_list.html │   │   │   └── timeline.html │   │   ├── init.py │   │   ├── admin.py │   │   ├── apps.py │   │   ├── models.py                  # NASAChallenge, Hito, Innovacion │   │   ├── tests.py │   │   ├── urls.py │   │   └── views.py │   │ │   ├── puntos_reciclaje/              # App puntos de recolección │   │   ├── migrations/ │   │   ├── templates/puntos_reciclaje/ │   │   │   ├── index.html │   │   │   ├── mapa.html │   │   │   ├── punto_detail.html │   │   │   └── solicitar_recoleccion.html │   │   ├── init.py │   │   ├── admin.py │   │   ├── apps.py │   │   ├── models.py                  # PuntoReciclaje, Recoleccion │   │   ├── tests.py │   │   ├── urls.py │   │   └── views.py │   │ │   ├── blog/                          # App blog educativo │   │   ├── migrations/ │   │   ├── templates/blog/ │   │   │   ├── index.html │   │   │   ├── post_detail.html │   │   │   └── categoria_posts.html │   │   ├── init.py │   │   ├── admin.py │   │   ├── apps.py │   │   ├── models.py                  # Categoria, Post, Comentario │   │   ├── tests.py │   │   ├── urls.py │   │   └── views.py │   │ │   ├── static/                        # Archivos estáticos globales │   │   ├── css/ │   │   ├── js/ │   │   └── img/ │   │ │   ├── staticfiles/                   # Archivos recolectados (producción) │   └── media/                         # Archivos subidos por usuarios │       ├── raee/ │       ├── miembros/ │       ├── proyectos/ │       ├── innovaciones/ │       └── blog/ │ ├── populate_db.py                     # Script para poblar base de datos ├── requirements.txt                   # Dependencias Python └── README.md                          # Este archivo

---