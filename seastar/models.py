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

class Puesto(models.Model):
    nombre_puesto = models.CharField(max_length=100)
    descripcion_puesto = models.TextField()

class Tripulante(models.Model):
    nombre_tripulante = models.CharField(max_length=100)
    legajo = models.CharField(max_length=10)
    navio_asignado = models.ForeignKey(Navio, on_delete=models.CASCADE)
    puesto_tripulante = models.ForeignKey(Puesto, on_delete=models.CASCADE)
    nombre_jefe = models.CharField(max_length=100)

class Pais(models.Model):
    nombre_pais = models.CharField(max_length=100)
    descripcion_pais = models.TextField()
    moneda = models.CharField(max_length=50)
    idioma = models.CharField(max_length=50)

class Ciudad(models.Model):
    nombre_ciudad = models.CharField(max_length=100)
    descripcion_ciudad = models.TextField()
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)

class Viaje(models.Model): ...

class Camarote(models.Model):
    tiposdecamarotes = ...
    tipo_camarote = models.CharField(max_length=100)
    ubicacion_camarote = models.IntegerField()
    numero_camarote = models.IntegerField()

class Pasajero(models.Model):
    tipo_documento = models.CharField(max_length=100)
    numero_documento = models.IntegerField()
    nombre = models.CharField(max_length=100)
    pais_origen = models.ForeignKey(Pais, on_delete=models.CASCADE)
    ciudad_origen = models.ForeignKey(Ciudad, on_delete=models.CASCADE)
    viaje_realizado = models.ForeignKey(Viaje, on_delete=models.CASCADE)
    camarote_alojado = models.ForeignKey(Camarote, on_delete=models.CASCADE)