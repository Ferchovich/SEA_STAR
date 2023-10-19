from django.shortcuts import render
from django.views.generic.list import ListView
from seastar.models import Tripulante, Navio, Itinerario, Puerto
# Create your views here.

def home(request):
    return render(request, "./index.html", {})

def about(request):
    itinerarios = Itinerario.objects.all()
    puertos = Puerto.objects.all()
    return render(request, "./about.html", { "itinerarios" : itinerarios ,  "puertos" : puertos })

def products(request):
    navios = Navio.objects.all()
    return render(request, "./products.html", { "navios" : navios })

def store(request):
    return render(request, "./store.html")

def login(request):
    login = Navio.objects.all()
    return render(request, "./login.html", { "login" : login })

