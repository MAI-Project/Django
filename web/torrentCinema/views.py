from django.shortcuts import render
from .models import Film, Category
from django.http import HttpResponse
# Create your views here.


def index(request):
    return render(request, 'main/index.html')


def comedy(request):
    c = Category.objects.get(name='comedy')
    film_list = c.film_set.all()
    return render(request, 'main/comedy.html', {'title': 'Comedy', 'films': film_list})


def drama(request):
    return render(request, 'main/drama.html')


def romance(request):
    return render(request, 'main/romance.html')


def detective(request):
    return render(request, 'main/detective.html')


def action(request):
    return render(request, 'main/action.html')


def player(request, filmId):
    film = Film.objects.get(pk=filmId)
    return render(request, 'main/player.html', {'film': film})


