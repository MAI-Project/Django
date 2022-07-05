from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return render(request, 'main/index.html')


def comedy(request):
    return render(request, 'main/comedy.html')


def drama(request):
    return render(request, 'main/drama.html')


def romance(request):
    return render(request, 'main/romance.html')


def detective(request):
    return render(request, 'main/detective.html')


def action(request):
    return render(request, 'main/action.html')


def player(request):
    return render(request, 'main/player.html')


