from django.db import models
from django.contrib.auth.models import User
import torrentCinema.models as filmModels

class Subscription(models.Model):
    owner = models.OneToOneField(User, related_name="subscription", on_delete=models.CASCADE)
    paid = models.BooleanField(default=False, null=True, verbose_name="Оплачена")

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'

class WatchLater(models.Model):
    owner = models.OneToOneField(User, related_name="owner", on_delete=models.CASCADE)
    film = models.ManyToManyField(filmModels.Film, related_name='watchList')