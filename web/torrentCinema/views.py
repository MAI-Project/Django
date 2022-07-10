from curses import flash
from django.shortcuts import render
from .models import Film, Category, Сomment
from django.http import HttpResponse

from django.contrib.auth.models import User
from django.contrib import auth

from django.http import StreamingHttpResponse
from django.shortcuts import render, get_object_or_404
from .services import open_file


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

    if film.from_torrent:      
        return render(request, 'main/player.html', {'film': film,"cat_list": p, 'comments': comments, 'isuser': isuser, 'userName': getUserName(request)})
    return render(request, 'main/localPayer.html', {'film': film,"cat_list": p, 'comments': comments, 'isuser': isuser, 'userName': getUserName(request)})


def getUserName(request):
    userName = ''
    if request.user:
        userName = request.user.username
    else:
        userName = ''
    return userName

def get_streaming_video(request, pk: int):
    file, status_code, content_length, content_range = open_file(request, pk)
    response = StreamingHttpResponse(file, status=status_code, content_type='video/mp4')

    response['Accept-Ranges'] = 'bytes'
    response['Content-Length'] = str(content_length)
    response['Cache-Control'] = 'no-cache'
    response['Content-Range'] = content_range
    return response