from django.db import models

class NASAChallenge(models.Model):
    """Información del proyecto NASA"""
    titulo = models.CharField(max_length=200)
    descripcion_corta = models.TextField(max_length=500)
    descripcion_completa = models.TextField()
    categoria_nasa = models.CharField(max_length=100)
    año = models.IntegerField()
    estado = models.CharField(max_length=50, default="En desarrollo")
    
    class Meta:
        verbose_name = "NASA Challenge"
        verbose_name_plural = "NASA Challenges"
    
    def __str__(self):
        return f"{self.titulo} ({self.año})"


class Hito(models.Model):
    """Hitos del proyecto NASA"""
    proyecto = models.ForeignKey(NASAChallenge, on_delete=models.CASCADE, related_name='hitos')
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha = models.DateField()
    completado = models.BooleanField(default=False)
    orden = models.IntegerField(default=0)
    
    class Meta:
        verbose_name = "Hito"
        verbose_name_plural = "Hitos"
        ordering = ['orden', 'fecha']
    
    def __str__(self):
        return self.titulo


class Innovacion(models.Model):
    """Innovaciones tecnológicas del proyecto"""
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    tecnologia = models.CharField(max_length=100)
    aplicacion = models.TextField()
    imagen = models.ImageField(upload_to='innovaciones/', blank=True, null=True)
    proyecto = models.ForeignKey(NASAChallenge, on_delete=models.CASCADE, related_name='innovaciones')
    
    class Meta:
        verbose_name = "Innovación"
        verbose_name_plural = "Innovaciones"
    
    def __str__(self):
        return self.titulo