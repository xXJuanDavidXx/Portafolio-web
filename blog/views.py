from django.shortcuts import render, get_object_or_404
from .models import Post
import markdown
#from .filters import Filtro
from .forms import Buscar


def renderPosts(request):
    total_posts = Post.objects.count()
    #posts = Filtro(request.GET, queryset=Post.objects.order_by('-date'))

    if 'query' in request.GET:
        form = Buscar(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            category = form.cleaned_data.get('category', None)
            resultados = Post.objects.all()
            if query:
                resultados = resultados.filter(title__icontains=query)
            if category:
                resultados = resultados.filter(category=category)

    else:
        form = Buscar()
        resultados = Post.objects.all()


    return render(request, "blog.html", { "total_posts": total_posts, 'pagina_actual': 'blogs', 'form': form, 'post': resultados})


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, "post_detail.html", {"post": post})


	
