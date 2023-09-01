from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Navio,)

class NavioAdmin(admin.ModelAdmin):
    def get_navio_name(self,obj):
        return obj.Navio.nombreNavio
    search_fields = ('nombreNavio','codigoNavio')
    list_display = ('nombreNavio','codigoNavio')
    list_filter = ('nombreNavio','codigoNavio',)
