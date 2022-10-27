from django.http import HttpResponse
from django.shortcuts import render

from blog.models import Articulo, Autor, Seccion, Avatar, Pagina
from blog.forms import ArticuloForm, AutorForm, SeccionForm, UserEditionForm, AvatarForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required 
def mostrar_inicio(request):
    avatar = Avatar.objects.filter(user=request.user).first()
    if avatar is not None:
        contexto = {"avatar": avatar.imagen.url}
    else:
        contexto = {}

    return render(request, "blog/inicio.html", contexto)


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
          




@login_required
def buscar_articulo(request):
    if request.method == "GET":
        return render(request, "blog/formulario-de-busqueda-articulo.html")

    if request.method == "POST":
        titulo_para_buscar = request.POST["titulo"]
        resultados_de_busqueda = Articulo.objects.filter(titulo=titulo_para_buscar)
        contexto = {"resultados": resultados_de_busqueda}
        return render(request, "blog/resultados-de-la-busqueda.html", context = contexto)

@login_required
def buscar_autor(request):
    if request.method == "GET":
        return render(request, "blog/formulario-de-busqueda-autor.html")

    if request.method == "POST":
        nombre_para_buscar = request.POST["nombre"]
        resultados_de_busqueda = Autor.objects.filter(nombre=nombre_para_buscar)
        contexto = {"resultados": resultados_de_busqueda}
        return render(request, "blog/resultados-de-la-busqueda.html", context = contexto)

@login_required
def buscar_seccion(request):
    if request.method == "GET":
        return render(request, "blog/formulario-de-busqueda-seccion.html")

    if request.method == "POST":
        nombre_para_buscar = request.POST["nombre_seccion"]
        resultados_de_busqueda = Seccion.objects.filter(nombre_seccion=nombre_para_buscar)
        contexto = {"resultados": resultados_de_busqueda}
        return render(request, "blog/resultados-de-la-busqueda.html", context = contexto)


class AutorList(LoginRequiredMixin, ListView):
    model = Autor
    template_name = "blog/autor_list.html"

class PaginasList(LoginRequiredMixin, ListView):
    model = Pagina
    template_name = "blog/paginas_list.html"

class AutorDetalle(LoginRequiredMixin, DetailView):
    model = Autor
    template_name = "blog/autor_detalle.html"

class PaginaDetalle(LoginRequiredMixin, DetailView):
    model = Pagina
    template_name = "blog/pagina_detalle.html"

from django.urls import reverse

class AutorCreacion(LoginRequiredMixin, CreateView):
    model = Autor
    fields = ["nombre", "apellido", "profesion"]
    success_url = "/blog/autor/list"
    


class AutorUpdateView(LoginRequiredMixin, UpdateView):
    model = Autor
    success_url = "/blog/autor/list"
    fields = ["nombre", "apellido", "profesion"]

class AutorDelete(LoginRequiredMixin, DeleteView):
    model = Autor
    success_url = "/blog/autor/list"

class MyLogin(LoginView):
    template_name = "blog/login.html"

class MyLogout(LoginRequiredMixin, LogoutView):
    template_name = "blog/logout.html"

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username_capturado = form.cleaned_data["username"]
            form.save()

            return render(request, "blog/inicio.html", {"mensaje": f"Usuario: {username_capturado}"})

    else:
        form = UserCreationForm()
    
    return render(request, "blog/registro.html", {"form": form})

@login_required
def editar_perfil(request):
    user = request.user
    avatar = Avatar.objects.filter(user=request.user).first()

    if request.method != "POST":
        form = UserEditionForm(initial={"email": user.email})
    else:
        form = UserEditionForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user.email = data["email"]
            user.first_name = data["first_name"]
            user.last_name = data["last_name"]
            user.set_password(data["password1"])
            user.save()
            return render(request, "blog/inicio.html", {"avatar": avatar.imagen.url})

    contexto = {
    "user": user, 
    "form": form,
    "avatar": avatar.imagen.url
    }
    return render(request, "blog/editarPerfil.html", contexto)

@login_required
def agregar_avatar(request):
    if request.method != "POST":
        form = AvatarForm()
    else:
        form = AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            Avatar.objects.filter(user=request.user).delete()
            form.save()
            return render(request, "blog/inicio.html")

    contexto = {"form": form}
    return render(request, "blog/avatar_form.html", contexto)

@login_required
def about_me(request):
    return render(request, "blog/about_me.html")

