from pyexpat import model
from tabnanny import verbose
from unicodedata import category
from django.db import models

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
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, verbose_name='Категория')
    #TODO: добавить поле магнет ссылки и пути до файла

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'


        