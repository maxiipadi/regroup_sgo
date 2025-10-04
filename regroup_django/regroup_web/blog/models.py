from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

class Categoria(models.Model):
    """Categorías del blog"""
    nombre = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    descripcion = models.TextField(blank=True)
    
    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
    
    def __str__(self):
        return self.nombre


class Post(models.Model):
    """Posts del blog educativo"""
    titulo = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    contenido = models.TextField()
    resumen = models.TextField(max_length=300)
    imagen_destacada = models.ImageField(upload_to='blog/', blank=True, null=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, related_name='posts')
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    publicado = models.BooleanField(default=False)
    vistas = models.IntegerField(default=0)
    
    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ['-fecha_publicacion']
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titulo)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.titulo


class Comentario(models.Model):
    """Comentarios en posts"""
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comentarios')
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    contenido = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    aprobado = models.BooleanField(default=False)
    
    class Meta:
        verbose_name = "Comentario"
        verbose_name_plural = "Comentarios"
        ordering = ['fecha']
    
    def __str__(self):
        return f"Comentario de {self.nombre} en {self.post.titulo}"