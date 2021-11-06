from django.db import models
from django.db.models.deletion import SET_NULL

# Create your models here.


class Actor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name


class Movie(models.Model):
    active = models.BooleanField(default=True)

    name = models.CharField(verbose_name="Movie", max_length=50, unique=True)

    description = models.TextField(verbose_name="Description")

    likes = models.IntegerField(default=0, null=True)

    rate = models.PositiveBigIntegerField(default=0, null=True)

    production_date = models.DateField(null=True, blank=True)

    actors = models.ManyToManyField('Actor')

    poster = models.ImageField('movie/movie/images', null=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    comment = models.TextField()
    movie = models.ForeignKey('Movie', on_delete=SET_NULL, null=True)

    def __str__(self):
        return f"{self.movie} Review"
