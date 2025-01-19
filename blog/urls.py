from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path("", views.renderPosts, name="posts"),
    path("<int:post_id>", views.post_detail, name="post_detail"),
    path("Filtro/", views.filtro_por_categoria, name="categoria"),
]
