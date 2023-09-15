from django import forms

class CrearTripulante(forms.Form):
    name = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)
    descripcion = forms.CharField(widget=forms.Textarea, label="Ingresa una descripcion")

class Navio(forms.Form):
    codigoNavio = forms.IntegerField(label="Código")
    nombreNavio = forms.CharField(label="Nombre", max_length=50)
    altura = forms.FloatField(label="Altura")
    eslora = forms.FloatField(label="Eslora")
    manga = forms.FloatField(label="Manga")
    desplazamiento = forms.FloatField(label="Desplazamiento")
    autonomiaViaje = forms.FloatField(label="Autonomía de Viajes")
    cantidadCamarotes = forms.IntegerField(label="Cantidad de Camarotes")
    maxCantidadPasajeros = forms.IntegerField(label="Cantidad máxima de Pasajeros")
    cantidadMotores = forms.IntegerField(label="Cantidad de Motores")
    cantidadTripulantes = forms.IntegerField(label="Cantidad de Tripulantes")