import django_filters
from .models import Post, Category


class Filtro(django_filters.FilterSet):
    category = django_filters.ModelChoiceFilter(
        queryset=Category.objects.all(),
        label='',
    )

    class Meta:
        model = Post
        fields = ['category']

