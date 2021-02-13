from Produkty.views import *
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('kategorie/<id>/', kategoria, name='kategoria'),
    path('produkt/<id>/', produkt, name='produkt'),

]
