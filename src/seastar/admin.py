from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Navio,)
admin.site.register(Puesto,)
admin.site.register(Tripulante,)
admin.site.register(Pais,)
admin.site.register(Ciudad,)
admin.site.register(Camarote,)
admin.site.register(Cubierta,)
admin.site.register(Pasajero,)

class NavioAdmin(admin.ModelAdmin):
    search_fields = ('nombreNavio','codigoNavio')