from django.urls import path
from .views import idcard_list, idcard_detail

urlpatterns = [
    path('', idcard_list, name='idcard_list'),
    path('<slug:slug>/', idcard_detail, name='idcard_detail'),
]
