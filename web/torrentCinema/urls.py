from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('genre/<int:tag>/', views.genre, name='genre'),
    path('player/<int:filmId>/', views.player, name='player'),
    path('stream/<int:pk>/', views.get_streaming_video, name='stream'),
]
