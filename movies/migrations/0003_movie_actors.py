# Generated by Django 3.2.9 on 2021-11-06 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_actor'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='actors',
            field=models.ManyToManyField(to='movies.Actor'),
        ),
    ]
