# Generated by Django 4.0.4 on 2022-07-05 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('torrentCinema', '0007_сomment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='rating',
            field=models.IntegerField(null=True, verbose_name='Рейтинг'),
        ),
    ]
