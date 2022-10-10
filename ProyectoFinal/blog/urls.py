from django.contrib import admin
from django.urls import path, include

from blog.views import mostrar_inicio, procesar_formulario_autor, procesar_formulario_articulo, procesar_formulario_seccion, buscar_articulo, buscar_autor, buscar_seccion

urlpatterns = [
    path('inicio/', mostrar_inicio),
    path("formulario-autor/", procesar_formulario_autor),
    path("formulario-articulo/", procesar_formulario_articulo),
    path("formulario-seccion/", procesar_formulario_seccion),
    path("buscar-articulo/", buscar_articulo),
    path("buscar-autor/", buscar_autor),
    path("buscar-seccion/", buscar_seccion),

] 