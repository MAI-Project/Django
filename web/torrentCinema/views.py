from curses import flash
from django.shortcuts import render
from .models import Film, Category, Сomment
from django.http import HttpResponse

from django.contrib.auth.models import User
from django.contrib import auth


def index(request):
    c = Category.objects.filter(maincategory=True)
    return render(request, 'main/index.html',{"cat_list": c, 'userName': getUserName(request)})


def genre(request, tag):
    p = Category.objects.filter(maincategory=True)
    c = Category.objects.get(pk=tag)
    film_list = []
    if request.user.is_authenticated and request.user.subscription.paid:
        film_list = c.film_set.all()
    else:
        film_list = c.film_set.filter(primary = False)
        
    return render(request, 'main/genre.html', {'title': c.name, 'films': film_list, "cat_list": p, 'userName': getUserName(request)})


def player(request, filmId):

    film = Film.objects.get(pk=filmId)
    isuser = False
    if request.user.is_authenticated:
        isuser = True
        
    p = Category.objects.filter(maincategory=True)
    comments = film.commented_film.all()

    if request.method == "POST":
        _body = request.POST.get('comment')
        if _body != "":
            comment = Сomment(owner = request.user, film=film, body=_body)
            comment.save()
            
    return render(request, 'main/player.html', {'film': film,"cat_list": p, 'comments': comments, 'isuser': isuser, 'userName': getUserName(request)})


def getUserName(request):
    userName = ''
    if request.user:
        userName = request.user.username
    else:
        userName = ''
    return userName