from django.urls import path
from . import views

app_name = 'app_PChop'

urlpatterns = [
    # Ruta principal (dirige a la lista de productos)
    path('', views.listar_productos, name='listar_productos'), 

    # Rutas de Productos
    path('productos/', views.listar_productos, name='listar_productos'),
    path('producto/<int:producto_id>/', views.detalle_producto, name='detalle_producto'),
    path('producto/crear/', views.crear_producto, name='crear_producto'),
    path('producto/editar/<int:producto_id>/', views.editar_producto, name='editar_producto'),
    path('producto/borrar/<int:producto_id>/', views.borrar_producto, name='borrar_producto'),

    # Rutas de Categorías
    path('categorias/', views.listar_categorias, name='listar_categorias'),
    path('categoria/<int:categoria_id>/', views.detalle_categoria, name='detalle_categoria'),
    path('categoria/crear/', views.crear_categoria, name='crear_categoria'),
    path('categoria/editar/<int:categoria_id>/', views.editar_categoria, name='editar_categoria'),
    path('categoria/borrar/<int:categoria_id>/', views.borrar_categoria, name='borrar_categoria'),
]