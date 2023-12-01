from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import User
from django.contrib import  messages
from seastar.models import *
from datetime import date
# Create your views here.

def home(request:HttpRequest):
    logged_user = getLoggedUser(request)

    if not logged_user  == "Iniciar Sesion":
        user = User.objects.get(username=logged_user)
        
        return render(request, "./index.html", {"logged_user" : logged_user, "user":user})
    return render(request, "./index.html", {"logged_user" : logged_user})
def itinerarios(request):
    logged_user = getLoggedUser(request)
    
    itinerarios = Itinerario.objects.all()
    puertos = Puerto.objects.all()
    return render(request, "./itinerarios.html", { "itinerarios" : itinerarios ,  "puertos" : puertos , "logged_user": logged_user})

def navios(request):
    logged_user = getLoggedUser(request)

    navios = Navio.objects.all()
    return render(request, "./navios.html", { "navios" : navios, "logged_user": logged_user })

def reserva(request):
    logged_user = getLoggedUser(request)
    user = User.objects.filter(username=logged_user)[0]

    recorridos = Recorrido.objects.all()
    if request.method == 'POST':
        messages.success(request,("Yippie"))

        fecha = date.today()
        camaroteReservado = Camarote.objects.get(numero_camarote=request.POST['seleccionCamarote'])
        nombreUsuario = user.first_name
        pasajero = Pasajero.objects.get(nombre=nombreUsuario)
        recorridoReservado = Recorrido.objects.get(id=request.POST['seleccionRecorrido'])
        miReserva = ReservaCamarote.objects.create(fechaReserva=fecha,camaroteReservado=camaroteReservado,recorridoReservado=recorridoReservado)
        miReserva.listaPasajeros.add(pasajero)
        miReserva.save()
        return redirect('./reserva.html')
    else :
        return render(request, "./reserva.html", { "recorridos" : recorridos, "logged_user" :logged_user })
    
def reservaCubierta(request):
    logged_user = getLoggedUser(request)
    recorridos = Recorrido.objects.all()
    cubiertas = Cubierta.objects.all()
    camarotes = Camarote.objects.all()
    if request.method == 'POST':
        itemNavio = request.POST['seleccion']
        return render(request, "./reservaCubierta.html", { "recorridos" : recorridos , "cubiertas" : cubiertas , "camarotes" : camarotes , "itemNavio" : itemNavio , "logged_user": logged_user })
    
def reservaCamarote(request):
    logged_user = getLoggedUser(request)
    recorridos = Recorrido.objects.all()
    cubiertas = Cubierta.objects.all()
    camarotes = Camarote.objects.all()
    if request.method == 'POST':
        itemCubierta = int(request.POST['seleccionCubierta'])
        return render(request, "./reservaCamarote.html", { "recorridos" : recorridos , "cubiertas" : cubiertas , "camarotes" : camarotes , "itemCubierta" : itemCubierta , "logged_user": logged_user })

def login_user(request: HttpRequest):
    logged_user = getLoggedUser(request)
    if request.method == "GET" and request.session.get("user"):
        return redirect("./profile.html")
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            
            
            request.session["user"] = username
            
            return redirect('/reserva.html')  
        else:
            messages.success(request,("Las credenciales no coinciden"))
            return redirect('./login.html')
    else:
        return render(request, './login.html', {"logged_user" :logged_user})
    
def signup(request: HttpRequest):
    ciudades = Ciudad.objects.all()
    paises = Pais.objects.all()
    tipoDocumentos = TipoDocumento.objects.all()
    logged_user = getLoggedUser(request)
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        tipo_doc = request.POST['tipo_doc']
        num_doc = request.POST['num_doc']
        ciudad = request.POST['ciudad']
    
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
        
        tipo_docF = TipoDocumento.objects.get(nombreTipoDocumento=tipo_doc)
        ciudadF = Ciudad.objects.get(nombre_ciudad=ciudad)
        paisF = Pais.objects.get(nombre_pais=ciudadF.pais)
        
        myuser = User.objects.create_user(username, email, pass1)
        mypasagero = Pasajero(username=username ,tipo_documento=tipo_docF, numero_documento=num_doc, nombre=fname, ciudad_origen=ciudadF, pais_origen=paisF)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.is_active = True
        myuser.save()
        mypasagero.save()
        messages.success(request, "Su cuenta fue creada con éxito.")
        
        return redirect('./login.html')
    
    elif request.method == "GET":   
        return render(request, "./signup.html", {"ciudades" : ciudades ,  "paises" : paises , "tipoDocumentos" : tipoDocumentos , "logged_user" : logged_user})

def profile(request: HttpRequest):
    logged_user = getLoggedUser(request)
    user = User.objects.get(username=logged_user)
    pasajero = Pasajero.objects.get(username = user.username)
    
    return render(request, "profile.html", {"logged_user": logged_user, "user" : user, "pasajero": pasajero})


def tripulantes(request):
    logged_user = getLoggedUser(request)
    user = User.objects.get(username = logged_user)
    puestos = Puesto.objects.all()
    navios = Navio.objects.all()
    if not user.is_staff:
        messages.warning(request, ("No tienes los permisos para ingresar a esa página"))
        return redirect("/")
    if request.method == "GET":
        tripulantes = Tripulante.objects.all()
        
        return render(request, "tripulantes.html", {"logged_user" : logged_user, "tripulantes" : tripulantes, "puestos" : puestos, "navios" : navios})
    elif request.method == "POST":
        legajo = request.POST["legajo"]
        nombre = request.POST["nombre"]
        apellido = request.POST["apellido"]
        navio = request.POST["navio"]
        puesto = request.POST["puesto"]
        jefe = request.POST["jefe"]
        naviofull = Navio.objects.get(nombreNavio = navio)
        puestofull = Puesto.objects.get(nombre_puesto = puesto)

        Tripulante.objects.create(legajo=legajo, nombre=nombre, apellido=apellido, navio_asignado = naviofull, puesto_tripulante = puestofull, nombre_jefe = jefe)
        return redirect("/tripulantes.html")
        
def logout_view(request:HttpRequest):
    logout(request)
    return redirect("/")

def editarRecorridos(request):
    logged_user = getLoggedUser(request)
    user = User.objects.get(username = logged_user)
    if not user.is_staff:
        messages.warning(request, ("No tienes los permisos para ingresar a esa página"))
        return redirect("/")
    
    recorridos = Recorrido.objects.all()
    navios = Navio.objects.all()
    itinerarios = Itinerario.objects.all()
    reservas = ReservaCamarote.objects.all()
    if request.method == 'POST':
        num = request.POST['num']
        iti = request.POST['itinerario']
        nav = request.POST['navio']
        fecha = request.POST['fecha']
        duracion = request.POST['duracion']

        itiF = Itinerario.objects.get(nombreItinerario=iti)
        navF = Navio.objects.get(nombreNavio=nav)

        myRecorrido = Recorrido(numeroEscala=num,itinerarioRealizado=itiF,navioDelViaje=navF,fechaViaje=fecha,duracionViaje=duracion)
        myRecorrido.save()

    return render(request, "editarRecorridos.html", { "itinerarios" : itinerarios , "reservas" : reservas , "navios" : navios , "recorridos": recorridos , "logged_user": logged_user })

def editarReserva(request):
    logged_user = getLoggedUser(request)
    user = User.objects.get(username = logged_user)
    if not user.is_staff:
        messages.warning(request, ("No tienes los permisos para ingresar a esa página"))
        return redirect("/")
    recorridos = Recorrido.objects.all()
    reservas = ReservaCamarote.objects.all()
    return render(request, "editarReserva.html", { "recorridos": recorridos , "reservas" : reservas , "logged_user": logged_user })

def getLoggedUser(request: HttpRequest):
    return request.session.get("user", "Iniciar Sesion")

