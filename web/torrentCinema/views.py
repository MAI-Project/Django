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
    c = Category.objects.get(name='drama')
    film_list = c.film_set.all()
    return render(request, 'main/drama.html', {'title': 'Drama', 'films': film_list})


def romance(request):
    c = Category.objects.get(name='romance')
    film_list = c.film_set.all()
    return render(request, 'main/romance.html', {'title': 'Romance', 'films': film_list})


def detective(request):
    c = Category.objects.get(name='detective')
    film_list = c.film_set.all()
    return render(request, 'main/detective.html', {'title': 'Detective', 'films': film_list})


def action(request):
    c = Category.objects.get(name='action')
    film_list = c.film_set.all()
    return render(request, 'main/action.html', {'title': 'Action', 'films': film_list})


def player(request, filmId):
    film = Film.objects.get(pk=filmId)
    return render(request, 'main/player.html', {'film': film})


