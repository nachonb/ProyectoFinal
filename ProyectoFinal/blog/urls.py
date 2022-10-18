from django.contrib import admin
from django.urls import path, include

from blog.views import mostrar_inicio, procesar_formulario_autor, procesar_formulario_articulo, procesar_formulario_seccion, buscar_articulo, buscar_autor, buscar_seccion, AutorList, AutorDetalle, AutorCreacion, AutorUpdateView, AutorDelete

urlpatterns = [
    path('inicio/', mostrar_inicio),
    path("formulario-autor/", procesar_formulario_autor),
    path("formulario-articulo/", procesar_formulario_articulo),
    path("formulario-seccion/", procesar_formulario_seccion),
    path("buscar-articulo/", buscar_articulo),
    path("buscar-autor/", buscar_autor),
    path("buscar-seccion/", buscar_seccion),
    path("autor/list", AutorList.as_view(), name="AutorList"),
    path("r'(?P<pk>\d+)^$'", AutorDetalle.as_view(), name="AutorDetail"),
    path("autor-nuevo/", AutorCreacion.as_view(), name="AutorNew"),
    path("editar/<pk>", AutorUpdateView.as_view(), name="AutorUpdate"),
    path("borrar/<pk>", AutorDelete.as_view(), name="AutorDelete")
    ] 