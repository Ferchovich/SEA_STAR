from django.shortcuts import render
from seastar.models import Navio, Itinerario, Puerto
# Create your views here.

def home(request):
    return render(request, "./index.html", {})

def about(request):
    itinerarios = Itinerario.objects.all()
    puertos = Puerto.objects.all()
    return render(request, "./itinerarios.html", { "itinerarios" : itinerarios ,  "puertos" : puertos })

def products(request):
    navios = Navio.objects.all()
    return render(request, "./navios.html", { "navios" : navios })

def store(request):
    return render(request, "./store.html")

def login(request):
    login = Navio.objects.all()
    return render(request, "./login.html", { "login" : login })

def profile(request):
    return render(request, "profile.html")
