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
    path("", views.home, name="home"),
    path("itinerarios.html", views.itinerarios, name="itinerarios"),
    path("navios.html", views.navios, name="navios"),
    path("reserva.html", views.reserva, name="reserva"),
    path("reservaCubierta.html", views.reservaCubierta, name="reservaCubierta"),
    path("reservaCamarote.html", views.reservaCamarote, name="reservaCamarote"),
    path("login.html", views.login_user, name="login"),
    path("signup.html", views.signup, name="signup"),
    path("profile.html", views.profile, name="profile"),
    path("editarRecorridos.html", views.editarRecorridos, name="editarRecorridos"),
    path("editarReserva.html", views.editarReserva, name="editarReserva"),
    path("tripulantes.html", views.tripulantes, name="tripulantes"),
    path("logout.html", views.logout_view, name="logout")
]
