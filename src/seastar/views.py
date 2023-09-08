from django.shortcuts import render
from .forms import CrearTripulante
# Create your views here.

def crearTripulantes(request):
    return render(request, "seastar/base.html", { "form" : CrearTripulante})

def home(request):
    return render(request, "seastar/home.html", {})