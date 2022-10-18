from django.http import HttpResponse
from django.shortcuts import render

from blog.models import Articulo, Autor, Seccion
from blog.forms import ArticuloForm, AutorForm, SeccionForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

# Create your views here.

def mostrar_inicio(request):
    return render(request, "blog/inicio.html")


def procesar_formulario_autor(request):
    if request.method == "GET":
        mi_formulario = AutorForm()
        contexto= {"formulario": mi_formulario}
        return render(request, "blog/formulario-autor.html", context=contexto)

    if request.method == "POST":
        mi_formulario = AutorForm(request.POST)
        if mi_formulario.is_valid():
            datos_ingresados_por_usuario = mi_formulario.cleaned_data
            nuevo_modelo = Autor(
                nombre= datos_ingresados_por_usuario["nombre"],
                apellido= datos_ingresados_por_usuario["apellido"],
                profesion= datos_ingresados_por_usuario["profesion"], 
            )
            nuevo_modelo.save()

            return render(request, "blog/exito.html")




def procesar_formulario_articulo(request):
    if request.method == "GET":
        mi_formulario = ArticuloForm()
        contexto= {"formulario": mi_formulario}
        return render(request, "blog/formulario-articulo.html", context=contexto)

    if request.method == "POST":

        mi_formulario = ArticuloForm(request.POST)
        if mi_formulario.is_valid():
            datos_ingresados_por_usuario = mi_formulario.cleaned_data
            nuevo_modelo = Articulo(
                titulo= datos_ingresados_por_usuario["titulo"],
                texto= datos_ingresados_por_usuario["texto"],
                fecha= datos_ingresados_por_usuario["fecha"], 
            )
            nuevo_modelo.save()

            return render(request, "blog/exito.html")


        contexto= {"formulario": mi_formulario}
        return render(request, "blog/formulario-articulo.html", context=contexto)


def procesar_formulario_seccion(request):
    if request.method == "GET":
        mi_formulario = SeccionForm()
        contexto= {"formulario": mi_formulario}
        return render(request, "blog/formulario-seccion.html", context=contexto)

    if request.method == "POST":
        mi_formulario = SeccionForm(request.POST)
        if mi_formulario.is_valid():
            datos_ingresados_por_usuario = mi_formulario.cleaned_data
            nuevo_modelo = Seccion(
                nombre_seccion= datos_ingresados_por_usuario["nombre_seccion"],
            )
            nuevo_modelo.save()
            return render(request, "blog/exito.html")
          





def buscar_articulo(request):
    if request.method == "GET":
        return render(request, "blog/formulario-de-busqueda-articulo.html")

    if request.method == "POST":
        titulo_para_buscar = request.POST["titulo"]
        resultados_de_busqueda = Articulo.objects.filter(titulo=titulo_para_buscar)
        contexto = {"resultados": resultados_de_busqueda}
        return render(request, "blog/resultados-de-la-busqueda.html", context = contexto)

def buscar_autor(request):
    if request.method == "GET":
        return render(request, "blog/formulario-de-busqueda-autor.html")

    if request.method == "POST":
        nombre_para_buscar = request.POST["nombre"]
        resultados_de_busqueda = Autor.objects.filter(nombre=nombre_para_buscar)
        contexto = {"resultados": resultados_de_busqueda}
        return render(request, "blog/resultados-de-la-busqueda.html", context = contexto)


def buscar_seccion(request):
    if request.method == "GET":
        return render(request, "blog/formulario-de-busqueda-seccion.html")

    if request.method == "POST":
        nombre_para_buscar = request.POST["nombre_seccion"]
        resultados_de_busqueda = Seccion.objects.filter(nombre_seccion=nombre_para_buscar)
        contexto = {"resultados": resultados_de_busqueda}
        return render(request, "blog/resultados-de-la-busqueda.html", context = contexto)


class AutorList(ListView):
    model = Autor
    template_name = "blog/autor_list.html"

class AutorDetalle(DetailView):
    model = Autor
    template_name = "blog/autor_detalle.html"

from django.urls import reverse

class AutorCreacion(CreateView):
    model = Autor
    fields = ["nombre", "apellido", "profesion"]
    success_url = "/blog/autor/list"
    


class AutorUpdateView(UpdateView):
    model = Autor
    success_url = "/blog/autor/list"
    fields = ["nombre", "apellido", "profesion"]

class AutorDelete(DeleteView):
    model = Autor
    success_url = "/blog/autor/list"
