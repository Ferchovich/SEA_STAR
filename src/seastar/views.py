from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import  messages
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

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('./store.html')  
        else:
            messages.success(request,("Sos malisimo"))
            return redirect('./login.html')
    else:
        return render(request, './login.html', {})