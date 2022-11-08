from django.contrib import admin

# Register your models here.

from mensajes.models import Mensaje

admin.site.register(Mensaje)