from django.shortcuts import render
from django.http import HttpResponse
from .models import Produkty, Kategoria
# Create your views here.

def index(request):
    wszystkie = Produkty.objects.all()
    jeden =     Produkty.objects.get (pk=4)
    kat =       Produkty.objects.filter (kategoria =3)
    producent = Produkty.objects.filter(producent = 2)
    kat_name =  Kategoria.objects.get(id=1)
    kategorie = Kategoria.objects.all()
    null =      Produkty.objects.filter(kategoria__isnull = False)
    zawiera =   Produkty.objects.filter (opis__icontains= "myszka")
    dane = {"kategorie": kategorie}

    return render(request, "szablon.html", dane)

def kategoria(request,id):
    kategoria_user = Kategoria.objects.get(pk=id)
    return HttpResponse(kategoria_user.nazwa)

def produkt (request, id):
    produkt_user = Produkty.objects.get(pk=id)
    return HttpResponse(produkt_user)