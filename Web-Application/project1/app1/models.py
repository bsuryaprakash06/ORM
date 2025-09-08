from django.db import models
from django.contrib import admin

# Create your models here.

class Movies(models.Model):
    Movie_ID = models.IntegerField(primary_key=True)
    Movie_name = models.CharField(max_length=100)
    Release_date=models.DateField()
    Director=models. CharField(max_length=50)
    Actors=models. CharField(max_length=100)
 
class MoviesAdmin(admin.ModelAdmin):
    list_display = ('Movie_ID', 'Movie_name', 'Release_date', 'Director', 'Actors')