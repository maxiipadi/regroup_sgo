# 🚀 LEGION ALFA - NASA Space Apps Challenge 2025

![LEGION ALFA Logo](core/static/core/img/nasa_logo_white.png)

## 📋 Descripción del Proyecto

**LEGION ALFA** es un sistema innovador de reciclaje circular diseñado para garantizar la autosuficiencia de la primera tripulación humana en Marte. Desarrollado como respuesta al NASA Space Apps Challenge 2025, nuestro proyecto transforma el concepto de "basura" en un banco de recursos vitales para la supervivencia.

> *"En Marte, no existe la 'basura', solo materias primas en el lugar equivocado."*

### 🎯 Objetivo Principal

Crear una economía circular y sostenible que permita a una tripulación de 8 personas sobrevivir durante 3 años en el Cráter Jezero, Marte, reciclando 12,600 kg de residuos inorgánicos in-situ.

## 🏗️ Arquitectura del Sistema

### Módulos Principales

1. **MPP - Módulo de Procesamiento Primario**
   - Clasificación automatizada de residuos
   - Pre-tratamiento inicial de materiales
   - Identificación y separación por tipo

2. **MTF - Módulo de Transformación y Fabricación**
   - Conversión de materiales reciclados
   - Fabricación de componentes útiles
   - Procesos de manufactura in-situ

3. **MAR - Módulo de Almacenamiento y Reutilización**
   - Gestión inteligente de inventario
   - Distribución optimizada de recursos
   - Reintegración al ecosistema de la base

## 📊 Especificaciones Técnicas

| Parámetro | Valor |
|-----------|-------|
| **TRL (Technology Readiness Level)** | 4-5 |
| **Capacidad de Procesamiento** | 15 kg/día |
| **Eficiencia Energética** | 2.5 kWh/kg |
| **Tasa de Recuperación** | 85-92% |
| **Disponibilidad Operativa** | >95% |
| **Potencia Requerida** | 12 kW pico, 8 kW promedio |
| **Huella del Sistema** | 45 m² |

## 🎭 Escenarios de Aplicación

### Escenario 1: Renovaciones de la Residencia
- **Entrada**: Estructuras de aluminio, fibra de carbono, embalajes
- **Salida**: Lingotes metálicos, paneles compuestos, láminas aislantes
- **Impacto**: Reducción del 35% en necesidades de reabastecimiento

### Escenario 2: Celebraciones Cósmicas
- **Entrada**: Textiles, uniformes, bolsas térmicas
- **Salida**: Decoraciones, atuendos festivos, elementos de confort
- **Impacto**: Mejora en salud mental y cohesión de la tripulación

### Escenario 3: Descubrimientos Audaces
- **Entrada**: Componentes electrónicos, filtros EVA, cartuchos químicos
- **Salida**: Nuevos filtros, sustratos agrícolas, lubricantes, nanomateriales
- **Impacto**: Extensión de capacidad de misión en +18 meses

## 🤖 Conoce a Tachy

Tachy es la IA que opera el sistema LEGION ALFA. En la Tierra, luchó contra los RAEE (Residuos de Aparatos Eléctricos y Electrónicos). Ahora ha aceptado la misión más importante: llevar el reciclaje responsable a Marte y garantizar que el Planeta Rojo no repita los errores del pasado.

## 🛠️ Tecnologías Utilizadas

- **Backend**: Django 4.x, Python 3.x
- **Frontend**: Bootstrap 5, JavaScript ES6+
- **Animaciones**: CSS3, Typed.js
- **Iconografía**: Bootstrap Icons
- **Diseño**: Responsive Design, Mobile-First

## 📁 Estructura del Proyecto

## 📁 Estructura del Proyecto

```
LEGION-ALFA/
│
├── core/                          # Aplicación principal
│   ├── migrations/
│   ├── static/
│   │   └── core/
│   │       ├── css/
│   │       ├── js/
│   │       ├── img/
│   │       │   ├── nasa_logo_white.png
│   │       │   ├── portada_marte.jpg
│   │       │   ├── Tachy.png
│   │       │   └── legion-alfa-architecture.svg
│   │       └── pdf/
│   │           └── LEGION-ALFA-Regroup.pdf
│   ├── templates/
│   │   └── core/
│   │       ├── base.html
│   │       └── index.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── nasa_project/                  # Proyecto NASA Challenge
│   ├── migrations/
│   ├── templates/
│   │   └── nasa_project/
│   │       └── index.html         # Página principal del proyecto NASA
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── raee_info/                     # Información sobre residuos en Marte
│   ├── migrations/
│   ├── templates/
│   │   └── raee_info/
│   │       └── index.html         # Waste Management on Mars
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── cooperativa/                   # Sección de la cooperativa
│   ├── migrations/
│   ├── templates/
│   │   └── cooperativa/
│   │       ├── index.html
│   │       └── impacto.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── puntos_reciclaje/             # Puntos de reciclaje
│   ├── migrations/
│   ├── templates/
│   │   └── puntos_reciclaje/
│   │       └── index.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── blog/                          # Blog ambiental
│   ├── migrations/
│   ├── templates/
│   │   └── blog/
│   │       └── index.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── regroup/                       # Configuración del proyecto Django
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── manage.py
├── requirements.txt
├── README.md
└── .gitignore
```

## 🚀 Instalación y Uso

### Requisitos Previos
- Python 3.8+
- pip
- virtualenv (recomendado)

### Instalación
```bash
# Clonar el repositorio
git clone https://github.com/tu-usuario/legion-alfa.git
cd legion-alfa

# Crear entorno virtual
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Migraciones
python manage.py migrate

# Crear superusuario (opcional)
python manage.py createsuperuser

# Ejecutar servidor de desarrollo
python manage.py runserver

Acceder a: http://localhost:8000
📊 Métricas de Impacto

89% - Eficiencia de recuperación de materiales
40% - Reducción de energía vs métodos tradicionales
60% - Reducción en masa de reabastecimiento
+18 meses - Extensión de capacidad de misión

🌟 Características Destacadas

✅ Diseño modular y escalable
✅ Interfaz moderna y responsive
✅ Animaciones fluidas y efectos visuales
✅ Sistema de navegación intuitivo
✅ Documentación técnica completa
✅ Cumplimiento con estándares NASA-STD-3001

👥 Equipo
REGroup - Cooperativa de Reciclaje RAEE

Santiago del Estero, Argentina
Participantes del NASA Space Apps Challenge 2025

📄 Licencia
Este proyecto está bajo la Licencia MIT. Ver el archivo LICENSE para más detalles.

📞 Contacto

Email: regroup.sgo@gmail.com
Teléfono: +54 385 4992929
Ubicación: Santiago del Estero, Argentina

🔗 Enlaces Importantes

Presentación PDF
NASA Space Apps Challenge
Documentación Técnica

🙏 Agradecimientos
Agradecemos a la NASA por crear el Space Apps Challenge y por inspirar soluciones innovadoras para la exploración espacial. Este proyecto representa nuestro compromiso con un futuro sostenible tanto en la Tierra como en Marte.

LEGION ALFA - Forjando un futuro sostenible en el Planeta Rojo 🔴
Desarrollado con 💚 por el equipo REGroup
