from django.shortcuts import render
from django.http import Http404
from .models import Post
from django.shortcuts import get_object_or_404
from .models import Tag

from datetime import date

all_posts = [
    {
        "slug": "gatito-curioso",
        "image": "gato1.jpg",
        "author": "Fina",
        "date": date(2023, 5, 21),
        "title": "El Gatito Curioso",
        "excerpt": "Descubre cómo los gatos exploran el mundo con sus bigotes.",
        "content": "Los gatos usan sus bigotes para orientarse... 🐾"
    },
    {
        "slug": "gatos-y-las-cajas",
        "image": "gato2.jpg",
        "author": "Albert",
        "date": date(2023, 3, 10),
        "title": "¿Por qué a los gatos les encantan las cajas?",
        "excerpt": "Una caja vacía es el mejor juguete para un gato. ¿Sabes por qué?",
        "content": "Los gatos adoran las cajas por instinto de protección..."
    },
    {
        "slug": "dormilon-peludo",
        "image": "gato3.jpg",
        "author": "Marta",
        "date": date(2023, 6, 12),
        "title": "El arte de dormir: gatos y sus 16 siestas",
        "excerpt": "¿Sabías que un gato duerme hasta 16 horas al día?",
        "content": "Dormir les permite conservar energía para la caza (o los mimos)..."
    },
    {
        "slug": "ronroneo-magico",
        "image": "gato4.jpg",
        "author": "César",
        "date": date(2023, 7, 1),
        "title": "El misterioso poder del ronroneo",
        "excerpt": "Más que un sonido, es una forma de comunicación y curación.",
        "content": "El ronroneo puede ayudar a calmar el estrés humano..."
    },
    {
        "slug": "guardian-nocturno",
        "image": "gato5.jpg",
        "author": "Júlia",
        "date": date(2023, 4, 8),
        "title": "Mi gato y sus aventuras nocturnas",
        "excerpt": "Cuando apagas la luz... empieza su misión secreta.",
        "content": "¡Cazando sombras y defendiendo su territorio imaginario!"
    },
    {
        "slug": "gatos-negros-y-suerte",
        "image": "gato6.jpg",
        "author": "David",
        "date": date(2023, 9, 5),
        "title": "Gatos negros: ¿mala o buena suerte?",
        "excerpt": "En Japón dan buena suerte. ¿Y tú qué piensas?",
        "content": "La superstición occidental es injusta con estos peludos..."
    },
    {
        "slug": "gato-programador",
        "image": "gato7.jpg",
        "author": "Laia",
        "date": date(2023, 2, 15),
        "title": "Mi gato pisa el teclado... ¿me ayuda a programar?",
        "excerpt": "Cada línea que borra con su cola... ¡es arte moderno!",
        "content": "Quizá tiene su propio lenguaje de programación secreto..."
    },
    {
        "slug": "gatitos-bebes",
        "image": "gato8.jpg",
        "author": "Marc",
        "date": date(2023, 8, 19),
        "title": "Los primeros días de un gatito bebé",
        "excerpt": "Del ronroneo a los primeros saltitos.",
        "content": "Es un proceso hermoso verlos crecer y explorar el mundo..."
    },
    {
        "slug": "adoptar-un-gato",
        "image": "gato9.jpg",
        "author": "Carla",
        "date": date(2023, 10, 1),
        "title": "Adoptar un gato: guía para principiantes",
        "excerpt": "Cosas básicas que debes saber antes de adoptar a tu peludo.",
        "content": "Desde su comida hasta el arenero, todo cuenta para su bienestar."
    },
    {
        "slug": "gatos-y-tecnologia",
        "image": "gato10.jpg",
        "author": "Nil",
        "date": date(2023, 11, 6),
        "title": "¿Cómo interactúan los gatos con la tecnología?",
        "excerpt": "¿Tu gato caza el puntero del ratón o duerme sobre el router?",
        "content": "Los gadgets pueden ser su enemigo... o su nuevo juguete preferido."
    }
]

# views.py

def starting_page(request):
    latest_posts = Post.objects.order_by('-date')[:3]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })

def posts(request):
    all_posts = Post.objects.order_by('-date')
    return render(request, "blog/posts_list.html", {"posts": all_posts})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, "blog/post_detail.html", {"post": post})
from .models import Author

def authors_list(request):
    authors = Author.objects.all()
    return render(request, "blog/authors_list.html", {"authors": authors})


def author_detail(request, id):
    author = get_object_or_404(Author, id=id)
    return render(request, "blog/author_detail.html", {"author": author})

def tags_list(request):
    tags = Tag.objects.all()
    return render(request, "blog/tag_list.html", {"tags": tags})

def posts_by_tag(request, id):
    tag = Tag.objects.get(id=id)
    posts = tag.post_set.all()
    return render(request, "blog/tag_post.html", {
        "tag": tag,
        "posts": posts
    })
