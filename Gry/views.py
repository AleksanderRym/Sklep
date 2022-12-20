from django.shortcuts import render
from django.http import HttpResponse
from .models import Gry, Producent, Gatunek

# Create your views here.

def index(request):
    gatunki = Gatunek.objects.all()
    dane = {'gatunki' : gatunki}
    return render(request, 'szablon.html', dane)

def gatunek(request, id):
    gatunek_user = Gatunek.objects.get(pk=id)
    gatunek_gra = Gry.objects.filter(gatunek = gatunek_user)
    gatunki = Gatunek.objects.all()
    dane = {'gatunek_user' : gatunek_user,
            'gatunek_gra' : gatunek_gra,
            'gatunki': gatunki}
    return render(request, 'gatunek_gra.html', dane)

def gra(request, id):
    gra_user = Gry.objects.get(pk=id)
    gatunki = Gatunek.objects.all()
    dane = {'gra_user' : gra_user,
            'gatunki' : gatunki}
    return render(request, 'gra.html', dane)

def gra_nazwa(request):
    if request.method == 'GET':
        query = request.GET.get('q')
        gra_nazwa = Gry.objects.filter(nazwa=query).first()
        if gra_nazwa:
            id = gra_nazwa.id
            gra_user = Gry.objects.get(pk=id)
            gatunki = Gatunek.objects.all()
            dane = {'gra_user': gra_user,
                    'gatunki': gatunki}
            print(dane)
            return render(request, 'gra.html', dane)
        else:
            return render(request, 'gra.html', {'error': 'Nie znaleziono gry'})
