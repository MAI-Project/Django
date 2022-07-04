from django.contrib import admin
from .models import Film, Category


class FilmAdmin(admin.ModelAdmin):
    """Настройка админ панели для модели фильма"""
    list_display = ('id', 'name', 'releaseDate', 'category')


class CategoryAdmin(admin.ModelAdmin):
    """Настройка админ панели для модели категории фильма"""
    list_display = ('id', 'name')


admin.site.register(Film, FilmAdmin)
admin.site.register(Category, CategoryAdmin)