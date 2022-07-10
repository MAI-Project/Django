from django.contrib import admin
from .models import Subscription


class SubscriptionAdmin(admin.ModelAdmin):
    """Настройка админ панели для модели Подписки"""
    list_display = ('id', 'owner', 'paid')

admin.site.register(Subscription, SubscriptionAdmin)

