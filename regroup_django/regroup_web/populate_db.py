import os
import django
from datetime import date, datetime, timedelta
from decimal import Decimal

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'regroup_web.settings')
django.setup()

from django.contrib.auth.models import User
from raee_info.models import CategoriaRAEE, MaterialRecuperable, InfoRAEE
from cooperativa.models import Miembro, Proyecto, ImpactoAmbiental
from nasa_project.models import NASAChallenge, Hito, Innovacion
from puntos_reciclaje.models import PuntoReciclaje, Recoleccion
from blog.models import Categoria, Post

print("🚀 Iniciando población de la base de datos...\n")

# ==================== USUARIOS ====================
print("👤 Creando usuarios...")
admin_user, created = User.objects.get_or_create(
    username='admin',
    defaults={
        'email': 'admin@regroup.coop',
        'first_name': 'Admin',
        'last_name': 'REGroup',
        'is_staff': True,
        'is_superuser': True
    }
)
if created:
    admin_user.set_password('admin123')
    admin_user.save()
    print("  ✅ Superusuario creado: admin/admin123")
else:
    print("  ℹ️  Superusuario ya existe")

# Crear usuarios adicionales
usuarios_data = [
    {'username': 'maria.silva', 'first_name': 'María', 'last_name': 'Silva', 'email': 'maria@regroup.coop'},
    {'username': 'juan.perez', 'first_name': 'Juan', 'last_name': 'Pérez', 'email': 'juan@regroup.coop'},
    {'username': 'ana.gomez', 'first_name': 'Ana', 'last_name': 'Gómez', 'email': 'ana@regroup.coop'},
]

for user_data in usuarios_data:
    user, created = User.objects.get_or_create(
        username=user_data['username'],
        defaults=user_data
    )
    if created:
        user.set_password('password123')
        user.save()
        print(f"  ✅ Usuario creado: {user_data['username']}")

# ==================== CATEGORÍAS RAEE ====================
print("\n♻️  Creando categorías RAEE...")
categorias_raee = [
    {
        'nombre': 'Electrodomésticos',
        'descripcion': 'Heladeras, lavarropas, microondas, etc.',
        'icono': 'bi-house',
        'color': '#0ea5e9'
    },
    {
        'nombre': 'Informática',
        'descripcion': 'Computadoras, laptops, tablets, periféricos',
        'icono': 'bi-laptop',
        'color': '#10b981'
    },
    {
        'nombre': 'Telefonía',
        'descripcion': 'Teléfonos celulares, fijos y accesorios',
        'icono': 'bi-phone',
        'color': '#f59e0b'
    },
    {
        'nombre': 'Audio/Video',
        'descripcion': 'TVs, equipos de audio, cámaras',
        'icono': 'bi-tv',
        'color': '#8b5cf6'
    },
]

for cat_data in categorias_raee:
    cat, created = CategoriaRAEE.objects.get_or_create(
        nombre=cat_data['nombre'],
        defaults=cat_data
    )
    if created:
        print(f"  ✅ Categoría creada: {cat.nombre}")

# ==================== MATERIALES RECUPERABLES ====================
print("\n💎 Creando materiales recuperables...")
cat_informatica = CategoriaRAEE.objects.get(nombre='Informática')
cat_telefonia = CategoriaRAEE.objects.get(nombre='Telefonía')

materiales_data = [
    {'nombre': 'Cobre', 'simbolo_quimico': 'Cu', 'porcentaje_recuperacion': Decimal('15.5'), 'valor_mercado': Decimal('8.50'), 'categoria': cat_informatica},
    {'nombre': 'Oro', 'simbolo_quimico': 'Au', 'porcentaje_recuperacion': Decimal('0.02'), 'valor_mercado': Decimal('58000'), 'categoria': cat_informatica},
    {'nombre': 'Plata', 'simbolo_quimico': 'Ag', 'porcentaje_recuperacion': Decimal('0.1'), 'valor_mercado': Decimal('620'), 'categoria': cat_informatica},
    {'nombre': 'Aluminio', 'simbolo_quimico': 'Al', 'porcentaje_recuperacion': Decimal('8.5'), 'valor_mercado': Decimal('2.20'), 'categoria': cat_informatica},
    {'nombre': 'Plástico', 'simbolo_quimico': '', 'porcentaje_recuperacion': Decimal('20.0'), 'valor_mercado': Decimal('0.50'), 'categoria': cat_telefonia},
]

for mat_data in materiales_data:
    mat, created = MaterialRecuperable.objects.get_or_create(
        nombre=mat_data['nombre'],
        categoria=mat_data['categoria'],
        defaults=mat_data
    )
    if created:
        print(f"  ✅ Material creado: {mat.nombre}")

# ==================== INFO RAEE ====================
print("\n📚 Creando información RAEE...")
info_raee_data = [
    {
        'titulo': '¿Por qué es importante reciclar celulares?',
        'contenido': 'Un celular contiene más de 40 elementos de la tabla periódica, incluyendo metales preciosos como oro y plata. Reciclarlos evita la contaminación y recupera estos valiosos recursos.',
        'categoria': cat_telefonia
    },
    {
        'titulo': 'Cómo preparar tu computadora para reciclar',
        'contenido': 'Antes de reciclar tu computadora, asegurate de hacer un backup de tus datos y realizar un formateo completo del disco duro para proteger tu información personal.',
        'categoria': cat_informatica
    },
]

for info_data in info_raee_data:
    info, created = InfoRAEE.objects.get_or_create(
        titulo=info_data['titulo'],
        defaults=info_data
    )
    if created:
        print(f"  ✅ Info RAEE creada: {info.titulo}")

# ==================== MIEMBROS COOPERATIVA ====================
print("\n👥 Creando miembros de la cooperativa...")
maria = User.objects.get(username='maria.silva')
juan = User.objects.get(username='juan.perez')
ana = User.objects.get(username='ana.gomez')

miembros_data = [
    {
        'usuario': maria,
        'rol': 'fundador',
        'fecha_ingreso': date(2023, 1, 15),
        'especialidad': 'Gestión Ambiental',
        'biografia': 'Licenciada en Gestión Ambiental con 10 años de experiencia en reciclaje.'
    },
    {
        'usuario': juan,
        'rol': 'fundador',
        'fecha_ingreso': date(2023, 1, 15),
        'especialidad': 'Ingeniería Electrónica',
        'biografia': 'Ingeniero especializado en desarme y clasificación de componentes electrónicos.'
    },
    {
        'usuario': ana,
        'rol': 'cooperativista',
        'fecha_ingreso': date(2023, 6, 1),
        'especialidad': 'Educación Ambiental',
        'biografia': 'Profesora dedicada a la concientización sobre el reciclaje responsable.'
    },
]

for miembro_data in miembros_data:
    miembro, created = Miembro.objects.get_or_create(
        usuario=miembro_data['usuario'],
        defaults=miembro_data
    )
    if created:
        print(f"  ✅ Miembro creado: {miembro.usuario.get_full_name()}")

# ==================== PROYECTOS ====================
print("\n📁 Creando proyectos...")
maria_miembro = Miembro.objects.get(usuario=maria)
juan_miembro = Miembro.objects.get(usuario=juan)

proyecto, created = Proyecto.objects.get_or_create(
    nombre='Planta de Reciclaje RAEE - Fase 1',
    defaults={
        'descripcion': 'Construcción y puesta en marcha de la primera planta de reciclaje de RAEE en Santiago del Estero.',
        'estado': 'ejecucion',
        'fecha_inicio': date(2024, 1, 1),
        'presupuesto': Decimal('500000.00')
    }
)
if created:
    proyecto.responsables.add(maria_miembro, juan_miembro)
    print(f"  ✅ Proyecto creado: {proyecto.nombre}")

# ==================== IMPACTO AMBIENTAL ====================
print("\n📊 Creando datos de impacto ambiental...")
impactos_data = [
    {
        'fecha': date(2024, 9, 1),
        'toneladas_recicladas': Decimal('45.5'),
        'co2_evitado': Decimal('120.3'),
        'empleos_generados': 35,
        'dispositivos_procesados': 1250
    },
    {
        'fecha': date(2024, 8, 1),
        'toneladas_recicladas': Decimal('38.2'),
        'co2_evitado': Decimal('95.8'),
        'empleos_generados': 32,
        'dispositivos_procesados': 980
    },
    {
        'fecha': date(2024, 7, 1),
        'toneladas_recicladas': Decimal('41.7'),
        'co2_evitado': Decimal('105.2'),
        'empleos_generados': 30,
        'dispositivos_procesados': 1100
    },
]

for impacto_data in impactos_data:
    impacto, created = ImpactoAmbiental.objects.get_or_create(
        fecha=impacto_data['fecha'],
        defaults=impacto_data
    )
    if created:
        print(f"  ✅ Impacto registrado: {impacto.fecha.strftime('%B %Y')}")

# ==================== NASA CHALLENGE ====================
print("\n🚀 Creando proyecto NASA...")
challenge, created = NASAChallenge.objects.get_or_create(
    titulo='RAEE Sustentable: Aplicando Tecnología Espacial',
    defaults={
        'descripcion_corta': 'Proyecto que integra IA y sensores para optimizar el reciclaje de RAEE.',
        'descripcion_completa': 'REGroup presenta una solución innovadora que aplica tecnología espacial al reciclaje de RAEE. Utilizamos IA, visión por computadora y sensores IoT para clasificar y procesar residuos electrónicos de manera eficiente, reduciendo la contaminación y maximizando la recuperación de materiales.',
        'categoria_nasa': 'Sostenibilidad y Economía Circular',
        'año': 2024,
        'estado': 'En desarrollo'
    }
)
if created:
    print(f"  ✅ Challenge NASA creado: {challenge.titulo}")

# ==================== HITOS NASA ====================
print("\n🏁 Creando hitos del proyecto NASA...")
hitos_data = [
    {
        'proyecto': challenge,
        'titulo': 'Investigación y Planificación',
        'descripcion': 'Análisis de viabilidad técnica y definición de alcance del proyecto.',
        'fecha': date(2024, 8, 1),
        'completado': True,
        'orden': 1
    },
    {
        'proyecto': challenge,
        'titulo': 'Desarrollo del Prototipo de IA',
        'descripcion': 'Entrenamiento del modelo de inteligencia artificial para clasificación de componentes.',
        'fecha': date(2024, 9, 15),
        'completado': True,
        'orden': 2
    },
    {
        'proyecto': challenge,
        'titulo': 'Implementación de Sensores IoT',
        'descripcion': 'Instalación y calibración de sensores para monitoreo en tiempo real.',
        'fecha': date(2024, 10, 1),
        'completado': False,
        'orden': 3
    },
    {
        'proyecto': challenge,
        'titulo': 'Pruebas Piloto',
        'descripcion': 'Validación del sistema completo con casos reales de reciclaje.',
        'fecha': date(2024, 10, 15),
        'completado': False,
        'orden': 4
    },
]

for hito_data in hitos_data:
    hito, created = Hito.objects.get_or_create(
        proyecto=hito_data['proyecto'],
        titulo=hito_data['titulo'],
        defaults=hito_data
    )
    if created:
        print(f"  ✅ Hito creado: {hito.titulo}")

# ==================== INNOVACIONES ====================
print("\n💡 Creando innovaciones tecnológicas...")
innovaciones_data = [
    {
        'proyecto': challenge,
        'titulo': 'Sistema de Clasificación con IA',
        'descripcion': 'Red neuronal convolucional que identifica componentes electrónicos con 95% de precisión.',
        'tecnologia': 'Deep Learning - TensorFlow',
        'aplicacion': 'Clasificación automática de RAEE reduciendo tiempo de procesamiento en 70%.'
    },
    {
        'proyecto': challenge,
        'titulo': 'Red de Sensores IoT',
        'descripcion': 'Sistema de monitoreo en tiempo real del proceso de reciclaje.',
        'tecnologia': 'IoT - MQTT Protocol',
        'aplicacion': 'Optimización del flujo de trabajo y detección temprana de anomalías.'
    },
    {
        'proyecto': challenge,
        'titulo': 'Dashboard de Impacto',
        'descripcion': 'Plataforma web para visualización de métricas ambientales en tiempo real.',
        'tecnologia': 'React + Django REST',
        'aplicacion': 'Transparencia y trazabilidad del impacto ambiental generado.'
    },
]

for innov_data in innovaciones_data:
    innov, created = Innovacion.objects.get_or_create(
        proyecto=innov_data['proyecto'],
        titulo=innov_data['titulo'],
        defaults=innov_data
    )
    if created:
        print(f"  ✅ Innovación creada: {innov.titulo}")

# ==================== PUNTOS DE RECICLAJE ====================
print("\n📍 Creando puntos de reciclaje...")
puntos_data = [
    {
        'nombre': 'REGroup - Sede Central',
        'tipo': 'cooperativa',
        'direccion': 'Av. Belgrano 1234',
        'ciudad': 'Santiago del Estero',
        'provincia': 'Santiago del Estero',
        'codigo_postal': '4200',
        'latitud': Decimal('-27.783310'),
        'longitud': Decimal('-64.264090'),
        'telefono': '+54 385 123-4567',
        'email': 'central@regroup.coop',
        'horario': 'Lunes a Viernes: 8:00 - 18:00\nSábados: 9:00 - 13:00'
    },
    {
        'nombre': 'Punto Móvil - Centro',
        'tipo': 'movil',
        'direccion': 'Plaza Libertad',
        'ciudad': 'Santiago del Estero',
        'provincia': 'Santiago del Estero',
        'codigo_postal': '4200',
        'latitud': Decimal('-27.795000'),
        'longitud': Decimal('-64.260000'),
        'telefono': '+54 385 123-4568',
        'email': 'movil@regroup.coop',
        'horario': 'Miércoles y Sábados: 10:00 - 14:00'
    },
    {
        'nombre': 'Electrohogar del Norte',
        'tipo': 'comercio',
        'direccion': 'Av. Rivadavia 567',
        'ciudad': 'Santiago del Estero',
        'provincia': 'Santiago del Estero',
        'codigo_postal': '4200',
        'latitud': Decimal('-27.790000'),
        'longitud': Decimal('-64.270000'),
        'telefono': '+54 385 456-7890',
        'email': 'info@electrohogar.com',
        'horario': 'Lunes a Sábados: 9:00 - 20:00'
    },
]

for punto_data in puntos_data:
    punto, created = PuntoReciclaje.objects.get_or_create(
        nombre=punto_data['nombre'],
        defaults=punto_data
    )
    if created:
        print(f"  ✅ Punto creado: {punto.nombre}")

# ==================== RECOLECCIONES ====================
print("\n🚚 Creando registros de recolecciones...")
punto_central = PuntoReciclaje.objects.get(nombre='REGroup - Sede Central')

recolecciones_data = [
    {
        'punto': punto_central,
        'fecha': datetime(2024, 9, 15, 10, 30),
        'cantidad_kg': Decimal('125.5'),
        'tipo_residuos': 'Computadoras, monitores, teclados',
        'observaciones': 'Recolección programada de empresa local'
    },
    {
        'punto': punto_central,
        'fecha': datetime(2024, 9, 20, 14, 0),
        'cantidad_kg': Decimal('87.3'),
        'tipo_residuos': 'Celulares, tablets, cargadores',
        'observaciones': 'Campaña de recolección en escuela'
    },
]

for recol_data in recolecciones_data:
    recol, created = Recoleccion.objects.get_or_create(
        punto=recol_data['punto'],
        fecha=recol_data['fecha'],
        defaults=recol_data
    )
    if created:
        print(f"  ✅ Recolección registrada: {recol.fecha.strftime('%d/%m/%Y')}")

# ==================== CATEGORÍAS BLOG ====================
print("\n🏷️  Creando categorías del blog...")
categorias_blog_data = [
    {'nombre': 'Reciclaje', 'slug': 'reciclaje', 'descripcion': 'Tips y guías sobre reciclaje de RAEE'},
    {'nombre': 'Tecnología', 'slug': 'tecnologia', 'descripcion': 'Innovaciones tecnológicas aplicadas'},
    {'nombre': 'Sostenibilidad', 'slug': 'sostenibilidad', 'descripcion': 'Impacto ambiental y economía circular'},
    {'nombre': 'Cooperativismo', 'slug': 'cooperativismo', 'descripcion': 'Valores y experiencias cooperativas'},
]

for cat_data in categorias_blog_data:
    cat, created = Categoria.objects.get_or_create(
        slug=cat_data['slug'],
        defaults=cat_data
    )
    if created:
        print(f"  ✅ Categoría blog creada: {cat.nombre}")

# ==================== POSTS BLOG ====================
print("\n📝 Creando posts del blog...")
cat_reciclaje = Categoria.objects.get(slug='reciclaje')
cat_tecnologia = Categoria.objects.get(slug='tecnologia')
cat_sostenibilidad = Categoria.objects.get(slug='sostenibilidad')

posts_data = [
    {
        'titulo': '5 Razones para Reciclar tu Celular Viejo',
        'slug': '5-razones-para-reciclar-tu-celular-viejo',
        'contenido': '''Los celulares viejos son una mina de oro literal. Cada dispositivo contiene pequeñas cantidades de oro, plata, cobre y otros metales preciosos.

¿Sabías que se necesitan 41 celulares para recuperar 1 gramo de oro? Aunque suene poco, cuando hablamos de millones de dispositivos, la cantidad es significativa.

Además, los celulares contienen sustancias tóxicas como plomo, mercurio y cadmio que pueden contaminar el suelo y el agua si no se manejan correctamente.

En REGroup, procesamos estos dispositivos de manera segura y responsable, recuperando hasta el 98% de los materiales.''',
        'resumen': 'Descubrí por qué reciclar tu celular es importante para el medio ambiente y la economía.',
        'autor': admin_user,
        'categoria': cat_reciclaje,
        'publicado': True
    },
    {
        'titulo': 'Cómo la IA está Revolucionando el Reciclaje',
        'slug': 'como-la-ia-esta-revolucionando-el-reciclaje',
        'contenido': '''La inteligencia artificial está transformando la industria del reciclaje. En REGroup, utilizamos redes neuronales para clasificar componentes electrónicos con una precisión del 95%.

Nuestro sistema puede identificar más de 100 tipos diferentes de componentes en segundos, un trabajo que antes tomaba horas de clasificación manual.

Esto no solo aumenta la eficiencia, sino que también mejora la seguridad de nuestros trabajadores, reduciendo su exposición a materiales potencialmente peligrosos.

La tecnología que estamos desarrollando para el NASA Space Apps Challenge podría ser replicada en plantas de reciclaje de todo el mundo.''',
        'resumen': 'Conocé cómo usamos inteligencia artificial para hacer el reciclaje más eficiente.',
        'autor': maria,
        'categoria': cat_tecnologia,
        'publicado': True
    },
    {
        'titulo': 'Economía Circular: El Futuro del Consumo',
        'slug': 'economia-circular-el-futuro-del-consumo',
        'contenido': '''La economía circular propone un modelo donde los productos se diseñan para ser reutilizados, reparados y reciclados, en lugar de desechados.

Este enfoque contrasta con la economía lineal tradicional de "extraer, fabricar, usar, desechar". En REGroup, somos parte de este cambio.

Cada tonelada de RAEE que reciclamos evita la extracción de nuevos recursos naturales y reduce significativamente las emisiones de CO₂.

El futuro del consumo responsable pasa por adoptar estos principios en toda la cadena de valor.''',
        'resumen': 'Exploramos el concepto de economía circular y su importancia para el planeta.',
        'autor': ana,
        'categoria': cat_sostenibilidad,
        'publicado': True
    },
]

for post_data in posts_data:
    post, created = Post.objects.get_or_create(
        slug=post_data['slug'],
        defaults=post_data
    )
    if created:
        print(f"  ✅ Post creado: {post.titulo}")

print("\n" + "="*50)
print("✨ ¡Base de datos poblada exitosamente!")
print("="*50)
print("\n📊 Resumen:")
print(f"   • Usuarios: {User.objects.count()}")
print(f"   • Categorías RAEE: {CategoriaRAEE.objects.count()}")
print(f"   • Materiales: {MaterialRecuperable.objects.count()}")
print(f"   • Miembros: {Miembro.objects.count()}")
print(f"   • Proyectos: {Proyecto.objects.count()}")
print(f"   • Impactos: {ImpactoAmbiental.objects.count()}")
print(f"   • Challenges NASA: {NASAChallenge.objects.count()}")
print(f"   • Hitos: {Hito.objects.count()}")
print(f"   • Innovaciones: {Innovacion.objects.count()}")
print(f"   • Puntos de Reciclaje: {PuntoReciclaje.objects.count()}")
print(f"   • Recolecciones: {Recoleccion.objects.count()}")
print(f"   • Posts Blog: {Post.objects.count()}")
print("\n🔐 Credenciales de acceso:")
print("   Usuario: admin")
print("   Password: admin123")
print("\n🌐 Accedé al admin en: http://127.0.0.1:8000/admin/")
print("="*50)