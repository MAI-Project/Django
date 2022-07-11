# from tokenize import Comment
from django.contrib import admin
from .models import Film, Category, Сomment


class FilmAdmin(admin.ModelAdmin):
    """Настройка админ панели для модели фильма"""
    list_display = ('id', 'name', 'releaseDate', 'category')


class CategoryAdmin(admin.ModelAdmin):
    """Настройка админ панели для модели категории фильма"""
    list_display = ('id', 'name')

# class CommentAdmin(admin.ModelAdmin):
#     """Настройка админ панели для модели категории фильма"""
#     list_display = ('id', 'owner')



admin.site.register(Film, FilmAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Сomment)