from django.test import TestCase
from blog.models import Autor

# Create your tests here.

class ViewTestCase(TestCase):
    def test_crear_autor(self):
        Autor.objects.create(nombre="Nombre1", apellido="Apellido1", profesion="Profesion1")
        Autor.objects.create(nombre="Nombre2", apellido="Apellido2", profesion="Profesion2")
        todos_los_autores = Autor.objects.all()

        assert len(todos_los_autores) == 2
        assert todos_los_autores[0].nombre == "Nombre1"
        assert todos_los_autores[0].apellido == "Apellido1"
        assert todos_los_autores[0].profesion == "Profesion1"
        assert todos_los_autores[1].nombre == "Nombre2"
        assert todos_los_autores[1].apellido == "Apellido2"
        assert todos_los_autores[1].profesion == "Profesion2"

#para la entrega final son 3 unit test en total
#falta una pagina, una view que diga "about me" , que sea /about/ {ya esta creado y funciona}
#una vista pages/ que tenga vista de toods los blogs que contenga todas las paginas, al tocar "Leer más" te de detalle
#de forma similar a "Mis autores", que muestra toods los autores, que tenga la opción de "Leer más", que sea como el "Detalle" que tengo en autores
# en caso de que no haya blogs, que muestre un mensaje que diga que no hay blogs aún, {HECHO} 
# cada MODEL blog debe tener TITULO, SUBTITULO, CUERPO, AUTOR, FECHA, IMAGEN (imagen = models.ImageField(upload_to="avatares", null=True, blank=True) , ademas ir a Settings.py y agregar el MEDIA_URL y MEDIA_ROOT  )
# se debe poder Crear página. Modificar página. Borrar página. Crear perfil. Modificar perfil.
# Al momento de ingresar a la app en la ruta base "/" { HECHO }
# tener una app de mensajeria en la URL /messages/ , hacer otra app (python manage.py startapp mensajes )
# poner una Clase llamada Mensaje (models.Model)
# remitente = 
