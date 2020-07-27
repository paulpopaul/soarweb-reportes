from django.urls import path
from .views import post_list, post_detail, category_detail

urlpatterns = [
    path('', post_list, name='post_list'),
    path('<slug:slug>/', post_detail, name='post_detail'),
    path('category_detail/<slug:slug>/', category_detail, name='category_detail'),
]
