from django.db import models
from django.core.validators import FileExtensionValidator
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
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, verbose_name='Категория')
    primary = models.BooleanField(null=True, default=False, verbose_name='По подписке')

        
    from_torrent = models.BooleanField(null=True, default=True, verbose_name='Загрузка с торрента')
    imagePath = models.ImageField(upload_to='media/poster/', null=True, verbose_name='Путь до постера')
    magnet = models.TextField(max_length=1024, null=True, verbose_name='Магнет ссылка')
    localVideo =  models.FileField(upload_to='media/video/', validators=[FileExtensionValidator(allowed_extensions=['mp4'])], null = True)

    def __str__(self):
        return self.name

    @property
    def photo_url(self):
        if self.imagePath and hasattr(self.imagePath, 'url'):
            return self.imagePath.url

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