"""
URL configuration for gualdapop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import include, path
from django.conf import settings # Importamos la configuración de la aplicación
from django.conf.urls.static import static # Importamos la función para servir ficheros estáticos

from compraventa.views import ComprarView, detalle_articulo, listado_articulos, PublicarOfertaView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', listado_articulos, name='listado_articulos'),  # Página principal
    path('articulos/<int:id>', detalle_articulo, name='detalle_articulo'),
    path('publicar-oferta/', PublicarOfertaView.as_view(), name='publicar_oferta'),
    path('comprar/<int:id>', ComprarView.as_view(), name='comprar'),
    path('accounts/', include('django.contrib.auth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
