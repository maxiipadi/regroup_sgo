from django.db import models

class PuntoReciclaje(models.Model):
    """Puntos de recolección de RAEE"""
    TIPOS = [
        ('centro', 'Centro de Reciclaje'),
        ('movil', 'Punto Móvil'),
        ('comercio', 'Comercio Adherido'),
        ('cooperativa', 'Cooperativa'),
    ]
    
    nombre = models.CharField(max_length=200)
    tipo = models.CharField(max_length=20, choices=TIPOS)
    direccion = models.CharField(max_length=300)
    ciudad = models.CharField(max_length=100)
    provincia = models.CharField(max_length=100)
    codigo_postal = models.CharField(max_length=10)
    latitud = models.DecimalField(max_digits=9, decimal_places=6)
    longitud = models.DecimalField(max_digits=9, decimal_places=6)
    telefono = models.CharField(max_length=20)
    email = models.EmailField()
    horario = models.TextField()
    activo = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = "Punto de Reciclaje"
        verbose_name_plural = "Puntos de Reciclaje"
    
    def __str__(self):
        return f"{self.nombre} - {self.ciudad}"


class Recoleccion(models.Model):
    """Registro de recolecciones"""
    punto = models.ForeignKey(PuntoReciclaje, on_delete=models.CASCADE, related_name='recolecciones')
    fecha = models.DateTimeField()
    cantidad_kg = models.DecimalField(max_digits=8, decimal_places=2)
    tipo_residuos = models.CharField(max_length=200)
    observaciones = models.TextField(blank=True)
    
    class Meta:
        verbose_name = "Recolección"
        verbose_name_plural = "Recolecciones"
        ordering = ['-fecha']
    
    def __str__(self):
        return f"Recolección {self.punto.nombre} - {self.fecha.strftime('%d/%m/%Y')}"