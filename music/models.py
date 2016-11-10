from django.db import models

# Create your models here.


class Album(models.Model):
    album_name = models.CharField(max_length=20)
    artist_name = models.CharField(max_length=20)
    genre = models.CharField(max_length=20)
    logo = models.CharField(max_length=1000)


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=20)
    song_title = models.CharField(max_length=20)