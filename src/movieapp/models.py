from django.db import models

# Create your models here.
class Movie(models.Model):
    movie_name = models.CharField(max_length=120)
    movie_rating = models.DecimalField(max_digits=10,decimal_places=1)
    release_date = models.CharField(max_length=120)
    movie_duration = models.CharField(max_length=120)
    movie_description = models.TextField()

    def __str__(self):
        return self.movie_name
