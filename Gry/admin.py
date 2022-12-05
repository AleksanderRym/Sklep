from django.contrib import admin
from .models import Gry, Producent, Gatunek

# Register your models here.

admin.site.register(Gry)
admin.site.register(Producent)
admin.site.register(Gatunek)