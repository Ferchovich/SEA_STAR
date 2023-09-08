from django.shortcuts import render
from .forms import CrearTripulante
# Create your views here.
def Home():
    pass

def crearTripulantes(request):
    return render(request, "index.html", { "form" : CrearTripulante})