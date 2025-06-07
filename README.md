# BlogGatos

BlogGatos es una sencilla aplicación desarrollada con [Django](https://www.djangoproject.com/) como proyecto de aprendizaje. Consiste en un pequeño blog dedicado a los gatos donde se pueden consultar artículos, autores y etiquetas.

## Funcionalidades principales

- Listado de publicaciones con imagen y extracto.
- Página de detalle para cada entrada.
- Listado de autores y detalle de sus publicaciones.
- Filtro de artículos por etiqueta.

## Estructura del proyecto

- `bookoutlet/` contiene la configuración principal de Django y el archivo de rutas globales.
- `blog/` agrupa modelos, vistas, plantillas y archivos estáticos.

### Modelos destacados (`blog/models.py`)

```python
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
```

```python
class Post(models.Model):
    title = models.CharField(max_length=200)
    excerpt = models.TextField()
    image = models.CharField(max_length=100)
    date = models.DateField()
    slug = models.SlugField(unique=True)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name="posts")
    tags = models.ManyToManyField(Tag)
```

### Vistas y URLs

En `blog/views.py` se encuentran las funciones más relevantes:

```python
def starting_page(request):
    latest_posts = Post.objects.order_by('-date')[:3]
    return render(request, "blog/index.html", {"posts": latest_posts})


def posts(request):
    all_posts = Post.objects.order_by('-date')
    return render(request, "blog/posts_list.html", {"posts": all_posts})
```

Las rutas del proyecto se incluyen en `bookoutlet/urls.py`:

```python
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("blog.urls")),
]
```

## Requisitos

- Python 3.10 o superior
- Django 5

## Instalación

1. Clona este repositorio y entra en el directorio del proyecto.
2. Instala las dependencias con `pip install django`.
3. Ejecuta `python manage.py migrate` para preparar la base de datos.
4. (Opcional) Crea un superusuario con `python manage.py createsuperuser` para acceder al panel de administración.
5. Inicia el servidor de desarrollo con `python manage.py runserver`.
6. Abre `http://127.0.0.1:8000/` en tu navegador para ver el blog.

## Pruebas

Actualmente no hay pruebas automatizadas. Al ejecutar `python manage.py test` se muestra el mensaje **NO TESTS RAN**.

## Licencia

Este proyecto se ofrece únicamente con fines educativos y no especifica una licencia concreta.
