from django import forms

class CrearTripulante(forms.Form):
    name = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)
    descripcion = forms.CharField(widget=forms.Textarea, label="Ingresa una descripcion")