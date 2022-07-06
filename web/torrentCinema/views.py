from django.shortcuts import render
from .models import Film, Category
from django.http import HttpResponse
# Create your views here.


def index(request):
    c = Category.objects.filter(maincategory=True)
    return render(request, 'main/index.html',{"cat_list": c})


def genre(request, tag):
    p = Category.objects.filter(maincategory=True)
    c = Category.objects.get(pk=tag)
    film_list = c.film_set.all()
    return render(request, 'main/genre.html', {'title': c.name, 'films': film_list,"cat_list": p})


def player(request, filmId):
    p = Category.objects.filter(maincategory=True)
    film = Film.objects.get(pk=filmId)
    return render(request, 'main/player.html', {'film': film,"cat_list": p})


