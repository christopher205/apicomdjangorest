from django.contrib import admin
from apis.models import Celulares


class Celular(admin.ModelAdmin):

    lista = ('id', 'modelo', 'fabricante', 'ano')
    links_lista = ('id', 'modelo')
    proc_lista = 'modelo'


admin.site.register(Celulares, Celular)