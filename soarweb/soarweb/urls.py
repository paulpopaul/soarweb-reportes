"""soarweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from soarweb import settings
from django.conf.urls import include
from django.conf.urls.static import static
from django.views.generic import TemplateView



from .views import home
from contact.views import contact



urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),

    path('', home, name='home'),
    path('contact/', contact, name="contact"),
    path('blog/', include(('blogapp.urls', 'blogapp'), namespace='blogapp')),
    path('tarjeta/', include(('idcard.urls', 'idcard'), namespace='idcard')),
    path('soar360/', TemplateView.as_view(template_name="soar-vision/soar360.html"), name='soar360'),
    path('logo3d/', TemplateView.as_view(template_name="soar-vision/logo-3d.html"), name='logo3d'),
    path('fotogrametria/', TemplateView.as_view(template_name="soar-vision/soarmapa.html"), name='fotogrametria'),
    path('home/', TemplateView.as_view(template_name="home.html"), name='home'),
    path('nosotros/', TemplateView.as_view(template_name="nosotros.html"), name='nosotros'),
    path('servicios/', TemplateView.as_view(template_name="servicios.html"), name='servicios'),
    path('productos/', TemplateView.as_view(template_name="productos.html"), name='productos'),
    path('equipamiento/', TemplateView.as_view(template_name="equipamiento.html"), name='equipamiento'),
    path('clientes/', TemplateView.as_view(template_name="clientes.html"), name='clientes'),
    path('rubros/', TemplateView.as_view(template_name="rubros.html"), name='rubros'),
    path('certificacion/', TemplateView.as_view(template_name="certificacion.html"), name='certificacion'),
    path('responsabilidadsocial/', TemplateView.as_view(template_name="responsabilidadsocial.html"), name='responsabilidadsocial'),
    path('contacto/', TemplateView.as_view(template_name="contacto.html"), name='contacto'),
    path('informe/', TemplateView.as_view(template_name="informe/informe-base.html"), name='informe'),
    path('informe_list/', TemplateView.as_view(template_name="informe_list.html"), name='informe_list'),
    path('informe_detail/', TemplateView.as_view(template_name="informe_detail.html"), name='informe_detail'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
