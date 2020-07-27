from django.urls import path
from .views import contact

# Create your views here.

urlpatterns = [
    path('', contact, name="contact"),

]