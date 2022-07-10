from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Subscription

from django.contrib.auth.models import User
from django.contrib import auth


"""Регистрация пользователя"""
def registration(request):
    error = ""
    if request.method == "GET":
        return render(request, 'auth/registration.html', {'error': error})

    else:
        _login = request.POST.get('login')
        _password = request.POST.get('password')

        if _login == "" or _password == "":
            error = "login and password should not be empty"
            return render(request, 'auth/registration.html', {'error': error})
        
        if User.objects.filter(username=_login):
            error = "User with this name already exists"
            return render(request, 'auth/registration.html', {'error': error})
        
        user = User.objects.create_user(username = _login, password=_password)
        Subscription(owner = user, paid = True).save()
        auth.login(request, user)

        return redirect('home')


"""Аутентификация пользователя"""
def login(request):
    error = ""
    if request.method == "GET":
        return render(request, 'auth/login.html', {'error': error}) 
    else:
        _login = request.POST.get('login')
        _password = request.POST.get('password')
        user = auth.authenticate(request, username=_login, password=_password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            error = "There is no user with this name or password"
            return render(request, 'auth/login.html', {'error': error}) 


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