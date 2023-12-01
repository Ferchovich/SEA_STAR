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
admin.site.register(Puerto,)
admin.site.register(CategoriaItinerario,)
admin.site.register(Itinerario,)
admin.site.register(CambioPuerto,)
admin.site.register(CambioEstadoNavio,)
admin.site.register(TipoCamarote,)
admin.site.register(ReservaCamarote,)
admin.site.register(EstadoCamarote,)
admin.site.register(EstadoNavio,)
admin.site.register(Recorrido,)
admin.site.register(TipoDocumento,)

class NavioAdmin(admin.ModelAdmin):
    search_fields = ('nombreNavio','codigoNavio')