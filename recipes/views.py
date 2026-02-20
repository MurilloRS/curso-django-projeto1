from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'recipes/home.html')


def sobre(request):
    return HttpResponse("Esta é a página Sobre.")


def contato(request):
    return render(request, 'recipes/contato.html')

# Create your views here.
