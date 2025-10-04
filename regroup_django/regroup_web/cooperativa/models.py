from django.db import models
from django.contrib.auth.models import User

class Miembro(models.Model):
    """Miembros de la cooperativa"""
    ROLES = [
        ('fundador', 'Fundador'),
        ('cooperativista', 'Cooperativista'),
        ('voluntario', 'Voluntario'),
    ]
    
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    rol = models.CharField(max_length=20, choices=ROLES)
    fecha_ingreso = models.DateField()
    especialidad = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='miembros/', blank=True, null=True)
    biografia = models.TextField(blank=True)
    activo = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = "Miembro"
        verbose_name_plural = "Miembros"
    
    def __str__(self):
        return f"{self.usuario.get_full_name()} - {self.rol}"


class Proyecto(models.Model):
    """Proyectos de la cooperativa"""
    ESTADOS = [
        ('planificacion', 'En Planificación'),
        ('ejecucion', 'En Ejecución'),
        ('completado', 'Completado'),
        ('pausado', 'Pausado'),
    ]
    
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    estado = models.CharField(max_length=20, choices=ESTADOS)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(blank=True, null=True)
    presupuesto = models.DecimalField(max_digits=12, decimal_places=2)
    responsables = models.ManyToManyField(Miembro, related_name='proyectos')
    imagen = models.ImageField(upload_to='proyectos/', blank=True, null=True)
    
    class Meta:
        verbose_name = "Proyecto"
        verbose_name_plural = "Proyectos"
        ordering = ['-fecha_inicio']
    
    def __str__(self):
        return self.nombre


class ImpactoAmbiental(models.Model):
    """Registro del impacto ambiental mensual"""
    fecha = models.DateField()
    toneladas_recicladas = models.DecimalField(max_digits=10, decimal_places=2)
    co2_evitado = models.DecimalField(max_digits=10, decimal_places=2, help_text="Toneladas de CO2")
    empleos_generados = models.IntegerField()
    dispositivos_procesados = models.IntegerField()
    
    class Meta:
        verbose_name = "Impacto Ambiental"
        verbose_name_plural = "Impacto Ambiental"
        ordering = ['-fecha']
    
    def __str__(self):
        return f"Impacto {self.fecha.strftime('%B %Y')}"