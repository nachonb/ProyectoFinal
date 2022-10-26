from django.contrib import admin
from blog.models import Autor, Articulo, Seccion, Avatar, Pagina
# Register your models here.

admin.site.register(Articulo)
admin.site.register(Autor)
admin.site.register(Seccion)
admin.site.register(Avatar)
admin.site.register(Pagina)