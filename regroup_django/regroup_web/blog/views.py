from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import Post, Categoria, Comentario

def index(request):
    """Página principal del blog"""
    posts = Post.objects.filter(publicado=True).select_related('autor', 'categoria')
    categorias = Categoria.objects.all()
    
    context = {
        'posts': posts,
        'categorias': categorias,
    }
    return render(request, 'blog/index.html', context)

def post_detail(request, slug):
    """Detalle de un post"""
    post = get_object_or_404(Post, slug=slug, publicado=True)
    comentarios = post.comentarios.filter(aprobado=True)
    
    # Incrementar vistas
    post.vistas += 1
    post.save(update_fields=['vistas'])
    
    # Procesar comentario
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        contenido = request.POST.get('contenido')
        
        Comentario.objects.create(
            post=post,
            nombre=nombre,
            email=email,
            contenido=contenido
        )
        messages.success(request, '¡Comentario enviado! Será visible una vez aprobado.')
    
    context = {
        'post': post,
        'comentarios': comentarios,
    }
    return render(request, 'blog/post_detail.html', context)

def categoria_posts(request, slug):
    """Posts de una categoría"""
    categoria = get_object_or_404(Categoria, slug=slug)
    posts = Post.objects.filter(categoria=categoria, publicado=True)
    
    context = {
        'categoria': categoria,
        'posts': posts,
    }
    return render(request, 'blog/categoria_posts.html', context)