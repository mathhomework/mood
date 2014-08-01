from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class Listener(AbstractUser):
    pass


class Mood(models.Model):
    feel = models.CharField(max_length = 100, null = True, blank=True)
    listener = models.ManyToManyField(Listener, null=True, blank=True, related_name="listener_mood")

    def __unicode__(self):
        return u"{}".format(self.feel)

class Song(models.Model):
    title = models.CharField(max_length = 200)
    artist = models.CharField(max_length = 200)
    album = models.CharField(max_length = 200, null=True, blank = True)
    mood = models.ManyToManyField(Mood, null=True, blank = True, related_name="mood_song")
    # Are listeners actually related to songs? Or are they only related to songs THROUGH movies?
    listener = models.ManyToManyField(Listener, null= True, blank = True, related_name="listener_song")

    def __unicode__(self):
        return u"{}".format(self.title)

class Movie(models.Model):
    title = models.CharField(max_length = 200)
    song = models.ManyToManyField(Song, null = True,blank = True, related_name="song_movie")
    listener = models.ManyToManyField(Listener, null = True, blank = True, related_name="listener_movie")

    def __unicode__(self):
        return u"{}".format(self.title)
