
from django.shortcuts import render

from blogapp.models import Post
from contact import views


def home(request):
    post_list = Post.objects.all()
    context = {
        'post_list': post_list,
        'form': views.contact(request=request),
    }
    template = "base.html"
    return render(request, template, context)
