from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth.models import User
from django.contrib import auth


def check(request):
    if request.user.is_authenticated:
        return True
    else:
        return False

def getUser(request):
    return request.user

# def login(request, user):
    # auth.login(request, user)