from django.shortcuts import render
from .forms import CrearTripulante
from seastar.models import Tripulante, Navio
# Create your views here.

def home(request):
    return render(request, "./seastar/home.html", {})

def crearTripulantes(request):
    tripulantes = Tripulante.objects.all()
    return render(request, "./seastar/base.html", { "form" : CrearTripulante})

def verNavios(request):
    navios = Navio.objects.all()
    return render(request, "./seastar/navio.html", { "form" : verNavios})