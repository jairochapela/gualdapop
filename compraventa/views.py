from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from compraventa.forms import ComprarForm, PublicarOfertaForm

from compraventa.models import Articulo

# Create your views here.

def listado_articulos(request):
    # Obtenemos todos los artículos de la base de datos
    articulos = Articulo.objects.all()
    # Enviamos los artículos a la plantilla para que le de formato dentro del HTML
    return render(request, 'compraventa/listado_articulos.html', {'articulos': articulos})


def detalle_articulo(request, id):
    # Obtiene el artículo con el id indicado como clave primaria
    articulo = Articulo.objects.get(pk=id)
    # Mostrar detalle del artículo en la plantilla correspondiente
    return render(request, 'compraventa/detalle_articulo.html', {'articulo': articulo})


class PublicarOfertaView(LoginRequiredMixin, View):
    def get(self, request):
        form = PublicarOfertaForm()
        return render(request, 'compraventa/publicar_oferta.html', {'form': form})
    
    def post(self, request):
        form = PublicarOfertaForm(request.POST) # Recogida de los datos del formulario
        if form.is_valid():
            # Crear el artículo con los datos del formulario
            articulo = Articulo(
                nombre=form.cleaned_data['nombre'],
                descripcion=form.cleaned_data['descripcion'],
                precio=form.cleaned_data['precio'],
                vendedor=request.user
            )
            articulo.save() # Guardar el artículo en la base de datos
            return redirect('listado_articulos')
        else:
            return render(request, 'compraventa/publicar_oferta.html', {'form': form})
        
        
class ComprarView(LoginRequiredMixin, View):
    def get(self, request, id):
        articulo = Articulo.objects.get(pk=id)
        form = ComprarForm()
        return render(request, 'compraventa/comprar.html', {'articulo': articulo, 'form': form})
    
    def post(self, request, id):
        articulo = Articulo.objects.get(pk=id)
        form = ComprarForm(request.POST)
        if form.is_valid():
            articulo.vendido = True
            articulo.comprador = request.user
            articulo.save()
            return redirect('listado_articulos')
        else:
            return render(request, 'compraventa/comprar.html', {'articulo': articulo, 'form': form})