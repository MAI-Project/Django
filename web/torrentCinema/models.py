from pyexpat import model
from tabnanny import verbose
from threading import local
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    """ Модель категории фильма, связанная с фильмами"""

    name = models.CharField(max_length=255,verbose_name='Название')
    maincategory = models.BooleanField(default=True, verbose_name='Главная категория')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Film(models.Model):
    """Модель конкретного фильма"""

    name = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    releaseDate = models.DateField(null=True, verbose_name='Дата Публикации')
    rating = models.IntegerField( null=True, verbose_name='Рейтинг')
    from_torrent = models.BooleanField(null=True, default=True, verbose_name='Загрузка с торрента')
    imagePath = models.TextField(null=True, verbose_name='Путь до постера')
    magnet = models.TextField(max_length=1024, null=True, verbose_name='Магнет ссылка')
    # localPath = models.CharField(max_length=255, null=True, verbose_name='Локальный Путь')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, verbose_name='Категория')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'


class Сomment(models.Model):
    owner = models.ForeignKey(User, null=True, on_delete=models.CASCADE, verbose_name='Ссылка на автора')
    film  = models.ForeignKey(Film, related_name="commented_film", null=True, on_delete=models.CASCADE, verbose_name='Ссылка на фильм')
    body = models.TextField(verbose_name='Тело комментария')
    
    def __str__(self):
        return self.body
        # return (self.owner.login + self.film)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'