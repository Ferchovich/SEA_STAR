from django.shortcuts import render
from seastar.models import Tripulante, Navio
# Create your views here.

def home(request):
    return render(request, "index.html", {})

