from django.shortcuts import render, get_object_or_404
from .models import Article


# Create your views here.

def blog_list(request):
    articles = Article.objects.all()[:3]
    context = {'articles': articles}
    return render(request, 'blog/list.html', context)


def blog_detail(request, year, month, day, slug, id):
    article = get_object_or_404(Article, publish__year=year, publish__month=month, publish__day=day, slug=slug, id=id)
    context = {'article': article}
    return render(request, 'blog/detail.html', context)
