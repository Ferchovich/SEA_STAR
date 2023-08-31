from django.db import models

# Create your models here.

class Navio (models.Model):
    codigoNavio = models.IntegerField("Código")
    nombreNavio = models.CharField("Nombre", max_length=50)
    altura = models.FloatField("Altura")
    eslora = models.FloatField("Eslora")
    manga = models.FloatField("Manga")
    desplazamiento = models.FloatField("Desplazamiento")
    autonomiaViaje = models.FloatField("Autonomía de Viajes")
    cantidadCamarotes = models.IntegerField("Cantidad de Camarotes")
    maxCantidadPasajeros = models.IntegerField("Cantidad máxima de Pasajeros")
    cantidadMotores = models.IntegerField("Cantidad de Motores")
    cantidadTripulantes = models.IntegerField("Cantidad de Tripulantes")