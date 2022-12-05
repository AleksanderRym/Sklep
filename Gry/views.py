from django.shortcuts import render
from django.http import HttpResponse
from .models import Gry, Producent, Gatunek

# Create your views here.

def index(request):
    wszystkie = Gry.objects.all()
    jeden = Gry.objects.get(pk=2)
    gat = Gry.objects.filter(gatunek=1)
    gat_name = Gatunek.objects.get(id=1)
    gatunki = Gatunek.objects.all()
    null = Gry.objects.filter(gatunek__isnull=True)
    dane = {'gatunki' : gatunki}
    return render(request, 'szablon.html', dane)

def gatunek(request, id):
    gatunek_user = Gatunek.objects.get(pk=id)
    return HttpResponse(gatunek_user)

def gra(request, id):
    gra_user = Gry.objects.get(pk=id)
    napis = "<h1>"+ str(gra_user) +"</h1>" + \
            "<p>" + str(gra_user.opis) + "</p>" + \
            "<p>"+ str(gra_user.cena) +"</p>"
    return HttpResponse(napis)