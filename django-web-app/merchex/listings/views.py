from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Band, Title


def index(request):
    return HttpResponse("Bonjour !, vous êtes à l'index.")

def hello(request):
    bands = Band.objects.all()
    titres = Title.objects.all()
    return render(request, 'listings/hello.html', {'first_band': bands[0], 'first_title': titres[0]}, )

def about_us(request):
    return HttpResponse("<h1>À propos</h1> <p>Nous adorons merch !</p>")

def listings(request):
    return HttpResponse("<h1>Listings</h1> <p>Voici les listings</p>")

def contact_us(request):
    return HttpResponse("<h1>Contactez-nous</h1> <p>Voici comment nous contacter</p>")
