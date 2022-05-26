from tkinter import CASCADE
from django.utils.timezone import now
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class PostBio(models.Model):
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=555)
    image = models.ImageField(upload_to='images_post',null=False,blank=False)
    date = models.DateTimeField(default=now, editable=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} {self.date} {self.author}"


class PostGames(models.Model):
    RESULT_CHOICES = (
    (1, '1-0'),
    (2, '0-1'),
    (3, '1/2-1/2'),
)
    title = models.CharField(max_length=255)
    title_players = models.CharField(max_length=255)
    result = models.IntegerField(choices=RESULT_CHOICES)
    content = models.CharField(max_length=555)
    image = models.ImageField(upload_to='images_post',null=False,blank=False)
    date = models.DateTimeField(default=now, editable=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} {self.date} {self.author}"

class PostPuzzles(models.Model):
    title = models.CharField(max_length=255, verbose_name='Título')
    solution = models.CharField(max_length=255, verbose_name='Solución del problema')
    content = models.CharField(max_length=555, verbose_name='Contenido adicional', null=True, blank=True)
    image = models.ImageField(upload_to='images_post',null=False,blank=False, verbose_name='Imágen del post')
    date = models.DateTimeField(default=now, editable=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} {self.date} {self.author}"
   