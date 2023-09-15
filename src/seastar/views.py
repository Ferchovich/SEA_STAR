from django.shortcuts import render
from seastar.models import Tripulante, Navio
# Create your views here.

def home(request):
    return render(request, "./seastar/home.html", {})

def navios(request):
    navios = Navio.objects.all()
    return render(request, "./seastar/navio.html", { "navios" : navios})

def Tripulante(request):
    tripulantes = Tripulante.objects.all()
    return render(request, "./seastar/base.html", { "form" : tripulantes})