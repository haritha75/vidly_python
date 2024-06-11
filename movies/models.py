# from django.db import models # this contains all the database activites

# # Create your models here.

from django.db import models
from django.utils import timezone

class Genre(models.Model):
    name = models.CharField(max_length=255,null=False)

    def __str__(self): # like to string method in java\
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=255,null=False)
    release_year = models.IntegerField()
    number_in_stock = models.IntegerField()
    daily_rate = models.FloatField() 
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)  # we can make relationsship between genre and movie
    date_created =  models.DateTimeField(default=timezone.now)

#  models are nothing but table naes in movies database now wwe have to store that models in dabase called dqlite3
