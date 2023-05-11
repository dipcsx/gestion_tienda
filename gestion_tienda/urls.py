from django.urls import path
from . import views

app_name = 'gestion_tienda'

urlpatterns=[
    path('',views.index,name='index'),
    path('gestionUsuario',views.gestionUsuario,name='gestionUsuario'),
    path('verProducto/<str:ind>',views.verProducto,name='verProducto'),
    path('cerrarSesion',views.cerrarSesion,name='cerrarSesion'),
    path('eliminarUsuario/<str:ind>',views.eliminarUsuario,name='eliminarUsuario'),
    path('nuevoProducto/<str:ind>',views.nuevoProducto,name='nuevoProducto'),
    path('eliminarProducto/<str:idProducto>&<str:idUsuario>',views.eliminarProducto,name='eliminarProducto')
]