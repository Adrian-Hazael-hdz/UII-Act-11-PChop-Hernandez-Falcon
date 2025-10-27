from django.db import models
from django.utils import timezone

class Categoria(models.Model):
    Nombre = models.CharField(max_length=100)
    Descripcion = models.TextField(blank=True, null=True)
    es_principal = models.BooleanField(default=False) 
    fecha_creacion = models.DateTimeField(default=timezone.now)
    icono = models.ImageField(upload_to='iconos_categorias/', blank=True, null=True) 

    def __str__(self):
        return self.Nombre

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"

class Producto(models.Model):
    Nombre = models.CharField(max_length=200)
    Descripcion = models.TextField()
    Precio = models.DecimalField(max_digits=10, decimal_places=2)
    Stock = models.IntegerField(default=0)
    URL_imagen = models.ImageField(upload_to='img_productos/', blank=True, null=True) 
    
    # RELACIÓN: ForeignKey con Categoria
    categoria = models.ForeignKey(
        Categoria, 
        on_delete=models.CASCADE,
        related_name='productos'
    )

    def __str__(self):
        return self.Nombre

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"