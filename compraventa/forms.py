from django.forms import ModelForm
from compraventa.models import Articulo

class PublicarOfertaForm(ModelForm):
    class Meta:
        model = Articulo
        fields = ['nombre', 'descripcion', 'precio']


class ComprarForm(ModelForm):
    class Meta:
        model = Articulo
        fields = []