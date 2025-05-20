from django.urls import path
from . import views

urlpatterns = [
    path('', views.starting_page, name='starting-page'),
    path('posts/', views.posts, name='posts-list'),
    path('posts/<slug:slug>/', views.post_detail, name='posts-detail-page'),
    path("authors/", views.authors_list, name="authors-list"),
    path("authors/<int:id>/", views.author_detail, name="author-detail"),
    path("tags/", views.tags_list, name="tags-list"),  # <- AÑADE ESTA
    path("tags/<int:id>/", views.posts_by_tag, name="tag-posts"),
]
