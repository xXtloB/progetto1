from django.contrib import admin

# Register your models here.
from .models import Autore,Libro,Genere

admin.site.register(Autore)
admin.site.register(Libro)
admin.site.register(Genere)