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
    nombre_puesto = models.CharField("Nombre Puesto",max_length=100)
    descripcion_puesto = models.TextField("Descripcion Puesto")

class Tripulante(models.Model):
    nombre_tripulante = models.CharField("Nombre Tripulante",max_length=100)
    legajo = models.CharField("Legajo",max_length=10)
    navio_asignado = models.ForeignKey("Navio Asignado",Navio, on_delete=models.CASCADE)
    puesto_tripulante = models.ForeignKey("Puesto Tripulante",Puesto, on_delete=models.CASCADE)
    nombre_jefe = models.CharField("Nombre Jefe",max_length=100)

class Pais(models.Model):
    nombre_pais = models.CharField("Nombre Pais",max_length=100)
    descripcion_pais = models.TextField("Descripcion Pais")
    moneda = models.CharField("Moneda",max_length=50)
    idioma = models.CharField("Idioma",max_length=50)

class Ciudad(models.Model):
    nombre_ciudad = models.CharField("Nombre Ciudad", max_length=100)
    descripcion_ciudad = models.TextField("Descripción Ciudad")
    pais = models.ForeignKey("Pais",Pais, on_delete=models.CASCADE)

class Camarote(models.Model):
    tiposdecamarotes = ...
    tipo_camarote = models.CharField("Tipo de Camarote", max_length=100)
    ubicacion_camarote = models.IntegerField("Ubicación Camarote")
    numero_camarote = models.IntegerField("Número Camarote")
    
class Cubierta(models.Model):
    numeroCubierta = models.IntegerField("Número Cubierta")
    ubicacionCubierta = models.CharField("Ubicación Cubierta", max_length=100)
    descripcionCubierta = models.CharField("Descripción Cubierta", max_length=200)
    encargado = models.ForeignKey("Encargado",Tripulante, on_delete=models.CASCADE)
    camarote = models.ForeignKey("Camarote",Camarote, on_delete=models.CASCADE)

class Pasajero(models.Model):
    tipo_documento = models.CharField("Tipo de Documento", max_length=100)
    numero_documento = models.IntegerField("Número de Documento")
    nombre = models.CharField("Nombre", max_length=100)
    pais_origen = models.ForeignKey("Pais Origen",Pais, on_delete=models.CASCADE)
    ciudad_origen = models.ForeignKey("Ciudad Origen",Ciudad, on_delete=models.CASCADE)
    camarote_alojado = models.ForeignKey("Camarote Alojado",Camarote, on_delete=models.CASCADE)