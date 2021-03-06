# Generated by Django 3.2.14 on 2022-07-10 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('torrentCinema', '0012_film_localpath'),
        ('authentication', '0003_watchlater'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watchlater',
            name='film',
            field=models.ManyToManyField(related_name='watchList', to='torrentCinema.Film'),
        ),
    ]
