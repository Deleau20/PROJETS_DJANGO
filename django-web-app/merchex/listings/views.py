from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello django.")

def about_us(request):
    return HttpResponse("<h1>À propos</h1> <p>Nous adorons merch !</p>")

def listings(request):
    return HttpResponse("<h1>Listings</h1> <p>Voici les listings</p>")

def contact_us(request):
    return HttpResponse("<h1>Contactez-nous</h1> <p>Voici comment nous contacter</p>")