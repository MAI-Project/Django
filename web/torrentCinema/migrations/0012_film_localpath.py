# Generated by Django 3.2.14 on 2022-07-10 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('torrentCinema', '0011_auto_20220710_1326'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='localPath',
            field=models.CharField(max_length=255, null=True, verbose_name='Локальный Путь'),
        ),
    ]
