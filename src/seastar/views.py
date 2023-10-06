from django.shortcuts import render
from seastar.models import Tripulante, Navio
# Create your views here.

def home(request):
    return render(request, "./index.html", {})

def about(request):
    return render(request, "./about.html")

def products(request):
    return render(request, "./products.html")

def store(request):
    return render(request, "./store.html")

def login(request):
    login = Navio.objects.all()
    return render(request, "./login.html", { "login" : login})

