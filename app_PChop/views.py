from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from .models import Producto, Categoria
from .forms import ProductoForm, CategoriaForm

# --- Vistas de Productos ---

def listar_productos(request):
    productos = Producto.objects.select_related('categoria').all()
    return render(request, 'productos_lista.html', {'productos': productos})

def detalle_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    return render(request, 'producto_detalle.html', {'producto': producto})

def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('app_PChop:listar_productos')
    else:
        form = ProductoForm()
    return render(request, 'formulario_producto.html', {'form': form, 'titulo': 'Crear Producto'})

def editar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('app_PChop:detalle_producto', producto_id=producto.id)
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'formulario_producto.html', {'form': form, 'titulo': f'Editar {producto.Nombre}'})

def borrar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        producto.delete()
        return redirect('app_PChop:listar_productos')
    return render(request, 'confirmar_borrar.html', {'objeto': producto, 'tipo': 'Producto'})


# --- Vistas de Categorías ---

def listar_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'categorias_lista.html', {'categorias': categorias})

def detalle_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    # Accedemos a los productos relacionados gracias al related_name='productos'
    productos = categoria.productos.all() 
    return render(request, 'categoria_detalle.html', {'categoria': categoria, 'productos': productos})

def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('app_PChop:listar_categorias')
    else:
        form = CategoriaForm()
    return render(request, 'formulario_categoria.html', {'form': form, 'titulo': 'Crear Categoría'})

def editar_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, request.FILES, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('app_PChop:detalle_categoria', categoria_id=categoria.id)
    else:
        form = CategoriaForm(instance=categoria)
    return render(request, 'formulario_categoria.html', {'form': form, 'titulo': f'Editar {categoria.Nombre}'})

def borrar_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    if request.method == 'POST':
        categoria.delete()
        return redirect('app_PChop:listar_categorias')
    return render(request, 'confirmar_borrar.html', {'objeto': categoria, 'tipo': 'Categoría'})