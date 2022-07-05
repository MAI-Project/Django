from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('registration/', views.registration, name="registration"),
    path('login/', views.login, name='login'),
    # path('check/', views.check, name='check'),
    path('logout/', views.logout, name='logout'),
]
