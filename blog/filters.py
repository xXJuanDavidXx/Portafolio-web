import django_filters
from django_filters import CharFilter, ModelChoiceFilter
from .models import Post, Category

class Filtro(django_filters.FilterSet):
    title = CharFilter(
        field_name='title', 
        lookup_expr='icontains', 
        label='Buscar por título'
    )

    category = ModelChoiceFilter(
        queryset=Category.objects.all(),
        label='Filtrar por categoría',
        empty_label="Todas las categorías"
    )

    class Meta:
        model = Post
        fields = ['title', 'category']
