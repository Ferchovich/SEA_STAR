from django.db import models

# Create your models here.

class CategoriaNavio(models.Model):
    nombreCategoria = models.CharField("Nombre de la Categoría", max_length=255)
    descripcionCategoria = models.TextField("Descripción de la Categoría")

    def __str__(self) -> str:
        return self.nombreCategoria

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
    categoriaNavio = models.ForeignKey(CategoriaNavio, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.nombreNavio

class Puesto(models.Model):
    nombre_puesto = models.CharField("Nombre Puesto",max_length=100)
    descripcion_puesto = models.TextField("Descripcion Puesto")

    def __str__(self) -> str:
        return self.nombre_puesto

class Tripulante(models.Model):
    nombre_tripulante = models.CharField("Nombre Tripulante",max_length=100)
    legajo = models.CharField("Legajo",max_length=10)
    navio_asignado = models.ForeignKey(Navio, on_delete=models.CASCADE)
    puesto_tripulante = models.ForeignKey(Puesto, on_delete=models.CASCADE)
    nombre_jefe = models.CharField("Nombre Jefe",max_length=100)

    def __str__(self) -> str:
        return self.nombre_tripulante

class Pais(models.Model):
    nombre_pais = models.CharField("Nombre Pais",max_length=100)
    descripcion_pais = models.TextField("Descripcion Pais")
    moneda = models.CharField("Moneda",max_length=50)
    idioma = models.CharField("Idioma",max_length=50)

    def __str__(self) -> str:
        return self.nombre_pais

class Ciudad(models.Model):
    nombre_ciudad = models.CharField("Nombre Ciudad", max_length=100)
    descripcion_ciudad = models.TextField("Descripción Ciudad")
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.nombre_ciudad
    
class TipoCamarote(models.Model):
    nombreTipoCamarote = models.CharField("Tipo de Camarote", max_length=255)
    descripcionTipoCamarote = models.TextField("Descripción del Tipo de Camarote")

    def __str__(self) -> str:
        return self.nombreTipoCamarote
    
class EstadoCamarote(models.Model):
    nombreEstadoCamarote = models.CharField("Estado del Camarote", max_length=255)
    descripcionEstadoCamarote = models.TextField("Descripción del Estado del Camarote")

    def __str__(self) -> str:
        return self.nombreEstadoCamarote
    
class Cubierta(models.Model):
    numeroCubierta = models.IntegerField("Numero Cubierta")
    ubicacionCubierta = models.CharField("Ubicación Cubierta", max_length=100)
    descripcionCubierta = models.CharField("Descripción Cubierta", max_length=200)
    encargado = models.ForeignKey(Tripulante, on_delete=models.CASCADE)
    navioUbicado = models.ForeignKey(Navio, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.numeroCubierta}'
    
class Camarote(models.Model):
    ubicacion_camarote = models.IntegerField("Ubicación Camarote")
    numero_camarote = models.IntegerField("Número Camarote")
    tipo_camarote = models.ForeignKey(TipoCamarote, on_delete=models.CASCADE)
    estadoCamarote = models.ForeignKey(EstadoCamarote, on_delete=models.CASCADE)
    cubiertaUbicada = models.ForeignKey(Cubierta, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.numero_camarote}'
    
class TipoDocumento(models.Model):
    nombreTipoDocumento = models.CharField("Tipo de Documento", max_length=100)
    descripcionTipoDocumento = models.CharField("Descripción del Tipo de Documento", max_length=200)

    def __str__(self) -> str:
        return self.nombreTipoDocumento

class Pasajero(models.Model):
    tipo_documento = models.ForeignKey(TipoDocumento, on_delete=models.CASCADE)
    numero_documento = models.IntegerField("Numero de Documento")
    username = models.CharField("Usuario", max_length=50, null=False, default="default")
    nombre = models.CharField("Nombre", max_length=100)
    pais_origen = models.ForeignKey(Pais, on_delete=models.CASCADE)
    ciudad_origen = models.ForeignKey(Ciudad, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.nombre

class Puerto(models.Model):
    nombrePuerto = models.CharField("Nombre del Puerto", max_length=255)
    descripcionPuerto = models.TextField("Descripción del Puerto")

    def __str__(self) -> str:
        return self.nombrePuerto

class CategoriaItinerario(models.Model):
    nombreCategoria = models.CharField("Nombre de la Categoría", max_length=255)
    descripcionCategoria = models.TextField("Descripción de la Categoría")

    def __str__(self) -> str:
        return self.nombreCategoria

class Itinerario(models.Model):
    nombreItinerario = models.CharField("Nombre del Itinerario", max_length=255)
    descripcionItinerario = models.TextField("Descripción del Itinerario")
    listaPuertos = models.ManyToManyField(Puerto)
    categoriaItinerario = models.ForeignKey(CategoriaItinerario, on_delete=models.CASCADE)

    def conocerCategoriaItinerario(self):
        pass

    def __str__(self) -> str:
        return self.nombreItinerarioz
    
class EstadoNavio(models.Model):
    nombreEstadoNavio = models.CharField("Estado del Navío", max_length=255)
    descripcionEstadoNavio = models.TextField("Descripción del Estado del Navío")

    def __str__(self) -> str:
        return self.nombreEstadoNavio

class HistorialTripulante(models.Model):
    tripulanteCambiado = models.ForeignKey(Tripulante, on_delete=models.CASCADE)
    nuevoPuestoTripulante = models.ForeignKey(Puesto, on_delete=models.CASCADE)
    nuevoNombreJefe = models.CharField("Nuevo Jefe", max_length=255)
    nuevoNavioAsignado = models.ForeignKey(Navio, on_delete=models.CASCADE)
    fechaCambio = models.DateTimeField("Fecha del cambio")

    def __str__(self) -> str:
        return f'{self.tripulanteCambiado} movído a {self.nuevoNavioAsignado}'

    def conocerPuesto(self):
        pass

class Recorrido(models.Model):
    numeroEscala = models.IntegerField("Numero Escala")
    itinerarioRealizado = models.ForeignKey(Itinerario, on_delete=models.CASCADE)
    navioDelViaje = models.ForeignKey(Navio, on_delete=models.CASCADE)
    fechaViaje = models.DateTimeField("Fecha de Inicio del viaje")
    duracionViaje = models.FloatField("Duración aproximada del viaje")

    def __str__(self) -> str:
        return f'Navío {self.navioDelViaje}, Fecha {self.fechaViaje}'

    def conocerNavio(self):
        pass

    def conocerCambioPuerto(self):
        pass

class ReservaCamarote(models.Model):
    fechaReserva = models.DateTimeField("Fecha de la reserva")
    recorridoReservado = models.ForeignKey(Recorrido, on_delete=models.CASCADE)
    camaroteReservado = models.ForeignKey(Camarote, on_delete=models.CASCADE)
    listaPasajeros = models.ManyToManyField(Pasajero)
    
    
    def __str__(self) -> str:
        return f'Reservas de la fecha {self.fechaReserva}'

    def agregarCamarote(self, camarote):
        self.listaCamarotes.add(camarote)

