from django.db import models

# Create your models here.
class Articulo(models.Model):
    nombre = models.CharField(max_length=100, blank=False, null=False)
    descripcion = models.TextField(blank=False, null=False)
    precio = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)
    fecha_publicacion = models.DateField(auto_now_add=True)
    vendido = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre


