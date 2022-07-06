from django.shortcuts import render
from .models import Film, Category
from django.http import HttpResponse
# Create your views here.


def index(request):
    return render(request, 'main/index.html')


def genre(request, tag):
    c = Category.objects.get(pk=tag)
    film_list = c.film_set.all()
    return render(request, 'main/genre.html', {'title': c.name, 'films': film_list})


def player(request, filmId):
    film = Film.objects.get(pk=filmId)
    return render(request, 'main/player.html', {'film': film})


