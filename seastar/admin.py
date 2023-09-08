from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Navio,)

class NavioAdmin(admin.ModelAdmin):
    search_fields = ('nombreNavio','codigoNavio')