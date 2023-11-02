from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import  messages
from seastar.models import Navio, Itinerario, Puerto, Recorrido, Cubierta, Camarote
# Create your views here.

logged_user = None
def home(request):
    
    return render(request, "./index.html", {"logged_user" : logged_user})

def about(request):
    itinerarios = Itinerario.objects.all()
    puertos = Puerto.objects.all()
    return render(request, "./itinerarios.html", { "itinerarios" : itinerarios ,  "puertos" : puertos , "logged_user": logged_user})

def products(request):
    navios = Navio.objects.all()
    return render(request, "./navios.html", { "navios" : navios })

def reserva(request):
    recorridos = Recorrido.objects.all()
    if request.method == 'POST':
        messages.success(request,("Yippie"))
        return redirect('./reserva.html')
    else :
        return render(request, "./reserva.html", { "recorridos" : recorridos })
    
def reservaCubierta(request):
    recorridos = Recorrido.objects.all()
    cubiertas = Cubierta.objects.all()
    camarotes = Camarote.objects.all()
    if request.method == 'POST':
        itemNavio = request.POST['seleccion']
        return render(request, "./reservaCubierta.html", { "recorridos" : recorridos , "cubiertas" : cubiertas , "camarotes" : camarotes , "itemNavio" : itemNavio })
    
def reservaCamarote(request):
    recorridos = Recorrido.objects.all()
    cubiertas = Cubierta.objects.all()
    camarotes = Camarote.objects.all()
    if request.method == 'POST':
        itemCubierta = int(request.POST['seleccionCubierta'])
        return render(request, "./reservaCamarote.html", { "recorridos" : recorridos , "cubiertas" : cubiertas , "camarotes" : camarotes , "itemCubierta" : itemCubierta })

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('./reserva.html')  
        else:
            messages.success(request,("Sos malisimo"))
            return redirect('./login.html')
    else:
        return render(request, './login.html', {})
    
def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
    
        if User.objects.filter(username=username):
            messages.error(request, "Ese nombre de usuario ya existe. Elija otro.")
            return redirect('./signup.html')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "La dirección de correo electrónico ya existe. Elija otra.")
            return redirect('./signup.html')
        
        if pass1 != pass2:
            messages.error(request, "Las contraseñas ingresadas no coinciden. Ingreselas nuevamente.")
            return redirect('./signup.html')
        
        if not username.isalnum():
            messages.error(request, "El nombre de usuario no puede contener caracteres especiales.")
            return redirect('./signup.html')
        
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.is_active = True
        myuser.save()
        messages.success(request, "Su cuenta fue creada con éxito.")
        
        return redirect('./login.html')
    
    else:   
        return render(request, "./signup.html", {})
