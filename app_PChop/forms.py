from django import forms
from .models import Producto, Categoria

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['Nombre', 'Descripcion', 'Precio', 'Stock', 'URL_imagen', 'categoria']

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['Nombre', 'Descripcion', 'es_principal', 'icono']