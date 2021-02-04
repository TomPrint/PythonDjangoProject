from django.shortcuts import render
from django.http import HttpResponse
from .models import Produkty
# Create your views here.

def index(request):
    zapytanie = Produkty.objects.all()
    return HttpResponse (zapytanie)
