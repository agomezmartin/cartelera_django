from django.shortcuts import render
from cartelera.models import Cartelera

# Create your views here.
def index(request):
    datos = Cartelera()
    cartelera = datos.series()

    series = {
        'cartelera' : cartelera
    }

    return render(request, 'index.html', series)