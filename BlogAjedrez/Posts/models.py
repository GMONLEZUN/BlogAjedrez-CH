from django.utils.timezone import now
from django.db import models

# Create your models here.


class PostBio(models.Model):
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=555)
    image = models.ImageField(upload_to='images_post',null=False,blank=False)
    date = models.DateTimeField(default=now, editable=False)

    def __str__(self):
        return f"{self.title} {self.date}"


class PostGames(models.Model):
    title = models.CharField(max_length=255)
    title_players = models.CharField(max_length=255)
    result = models.CharField(max_length=255)
    content = models.CharField(max_length=555)
    image = models.ImageField(upload_to='images_post',null=False,blank=False)
    date = models.DateTimeField(default=now, editable=False)

    def __str__(self):
        return f"{self.title} {self.date}"

class PostPuzzles(models.Model):
    title = models.CharField(max_length=255)
    solution = models.CharField(max_length=255)
    content = models.CharField(max_length=555)
    image = models.ImageField(upload_to='images_post',null=False,blank=False)
    date = models.DateTimeField(default=now, editable=False)

    def __str__(self):
        return f"{self.title} {self.date}"