from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Articulo(models.Model):
    nombre = models.CharField(max_length=100, blank=False, null=False)
    descripcion = models.TextField(blank=False, null=False)
    precio = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)
    fecha_publicacion = models.DateField(auto_now_add=True)
    vendido = models.BooleanField(default=False)
    foto = models.ImageField(upload_to='fotos', blank=True, null=True)
    vendedor = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='vendedor')
    comprador = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='comprador')

    def __str__(self):
        return self.nombre


