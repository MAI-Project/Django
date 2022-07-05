from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth.models import User
from django.contrib import auth

"""Регистрация пользователя"""
def registration(request):
    if request.method == "GET":
        return render(request, 'auth/registration.html')

    else:
        _login = request.POST.get('login')
        #TODO: переписать это гавон
        if User.objects.get(username=_login) is not None:
            return redirect('login')
        
        _password = request.POST.get('password')
        user = User.objects.create_user(username = _login, password=_password)
        auth.login(request, user)

        return redirect('home')

"""Аутентификация пользователя"""
def login(request):
    if request.method == "GET":
        return render(request, 'auth/login.html')  
    else:
        _login = request.POST.get('login')
        _password = request.POST.get('password')
        user = auth.authenticate(request, username=_login, password=_password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return redirect('registration')

"""Авторизация пользователя"""
def check(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        return redirect('login')

"""Выход пользователя из системы"""
def logout(request):
    auth.logout(request)
    return redirect('home')