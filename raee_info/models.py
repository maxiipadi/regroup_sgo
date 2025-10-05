from django.db import models

class CategoriaRAEE(models.Model):
    """Categorías de residuos electrónicos"""
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    icono = models.CharField(max_length=50, help_text="Clase de Bootstrap Icons")
    color = models.CharField(max_length=7, default="#0ea5e9")
    
    class Meta:
        verbose_name = "Categoría RAEE"
        verbose_name_plural = "Categorías RAEE"
    
    def __str__(self):
        return self.nombre


class MaterialRecuperable(models.Model):
    """Materiales que se pueden recuperar del reciclaje"""
    nombre = models.CharField(max_length=100)
    simbolo_quimico = models.CharField(max_length=10, blank=True)
    porcentaje_recuperacion = models.DecimalField(max_digits=5, decimal_places=2)
    valor_mercado = models.DecimalField(max_digits=10, decimal_places=2, help_text="USD por kg")
    categoria = models.ForeignKey(CategoriaRAEE, on_delete=models.CASCADE, related_name='materiales')
    
    class Meta:
        verbose_name = "Material Recuperable"
        verbose_name_plural = "Materiales Recuperables"
    
    def __str__(self):
        return f"{self.nombre} ({self.simbolo_quimico})"


class InfoRAEE(models.Model):
    """Información educativa sobre RAEE"""
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    imagen = models.ImageField(upload_to='raee/', blank=True, null=True)
    categoria = models.ForeignKey(CategoriaRAEE, on_delete=models.CASCADE, related_name='informacion')
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Información RAEE"
        verbose_name_plural = "Información RAEE"
        ordering = ['-fecha_publicacion']
    
    def __str__(self):
        return self.titulo