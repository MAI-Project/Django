# Generated by Django 4.0.4 on 2022-07-05 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('torrentCinema', '0002_remove_film_releasedate_film_from_torrent_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='imagePath',
            field=models.TextField(verbose_name='Путь до постера'),
        ),
        migrations.AlterField(
            model_name='film',
            name='magnet',
            field=models.TextField(verbose_name='Магнет ссылка'),
        ),
    ]
