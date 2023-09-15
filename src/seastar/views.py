from django.shortcuts import render
from .forms import CrearTripulante
from seastar.models import Tripulante
# Create your views here.

def home(request):
    return render(request, "./seastar/home.html", {})

def crearTripulantes(request):
    tripulante = Tripulante.objects.all()
    return render(request, "./  base.html", { "form" : CrearTripulante})