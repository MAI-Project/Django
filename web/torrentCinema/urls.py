from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('comedy', views.comedy, name='comedy'),
    path('drama', views.drama, name='drama'),
    path('romance', views.romance, name='romance'),
    path('detective', views.detective, name='detective'),
    path('action', views.action, name='action'),
    path('player', views.player, name='player'),
    path('player/<int:filmId>/', views.player, name='player')
]
