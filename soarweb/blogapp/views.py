from django.shortcuts import render, get_object_or_404
# Create your views here.
from .models import Post, Category


def post_list(request):
    template = 'blogapp/post_list.html'
    object_list = Post.objects.filter(status='Publicado')
    context = {
        'object_list': object_list,
    }
    return render(request, template, context)


def post_detail(request, slug):
    template = 'blogapp/post_detail.html'
    post = get_object_or_404(Post, slug=slug)
    context = {
        'post': post,
    }
    return render(request, template, context)


def category_detail(request, slug):
    template = 'blogapp/category_detail.html'
    category = get_object_or_404(Category, slug=slug)
    post = Post.objects.filter(category=category)
    context = {
        'category': category,
        'post': post,
    }
    return render(request, template, context)
