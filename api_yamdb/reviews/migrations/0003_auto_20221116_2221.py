# Generated by Django 3.2.16 on 2022-11-16 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_auto_20221116_0000'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='title',
            name='genre',
        ),
        migrations.AddField(
            model_name='title',
            name='genre',
            field=models.ManyToManyField(null=True, related_name='genres', to='reviews.Genre', verbose_name='Жанр произведения'),
        ),
    ]