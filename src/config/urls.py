"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from seastar import views
from seastar.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", HomeView.as_view(), name="home"),
    path("itinerarios.html", ItinerariosView.as_view(), name="itinerarios"),
    path("navios.html", NaviosView.as_view(), name="navios"),
    path("reserva.html", ReservaView.as_view(), name="reserva"),
    path("reservaCubierta.html", ReservaCubiertaView.as_view(), name="reservaCubierta"),
    path("reservaCamarote.html", ReservaCamaroteView.as_view(), name="reservaCamarote"),
    path("login.html", LoginView.as_view(), name="login"),
    path("signup.html", SignupView.as_view(), name="signup"),
    path("profile.html", ProfileView.as_view(), name="profile"),
    path("adminRecorridos.html", AdminRecorridosView.as_view(), name="adminRecorridos"),
    path("adminReserva.html", AdminReservaView.as_view(), name="adminReserva"),
    path("editarRecorridos.html", EditarRecorridosView.as_view(), name="editarRecorridos"),
    path("editarReserva.html", EditarReservaView.as_view(), name="editarReserva"),
    path("tripulantes.html", TripulantesView.as_view(), name="tripulantes"),
    path("logout.html", LogoutView.as_view(), name="logout")
]
