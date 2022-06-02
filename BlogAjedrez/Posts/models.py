from django.utils.timezone import now
from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.


class PostBio(models.Model):
    title = models.CharField(max_length=255)
    content = RichTextField(blank=True, null=True)
    image = models.ImageField(upload_to='images_post',null=False,blank=False)
    date = models.DateTimeField(default=now, editable=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name="blog_postsBio")
    def total_likesbio(self):
        return self.likes.count()

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
    content = RichTextField(blank=True, null=True)
    image = models.ImageField(upload_to='images_post',null=False,blank=False)
    date = models.DateTimeField(default=now, editable=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name="blog_postsGames")

    def total_likesgames(self):
        return self.likes.count()

    def __str__(self):
        return f"{self.title} {self.date} {self.author}"

class PostPuzzles(models.Model):
    title = models.CharField(max_length=255, verbose_name='Título')
    solution = models.CharField(max_length=255, verbose_name='Solución del problema')
    content = RichTextField(verbose_name='Contenido adicional', null=True, blank=True)
    image = models.ImageField(upload_to='images_post',null=False,blank=False, verbose_name='Imágen del post')
    date = models.DateTimeField(default=now, editable=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name="blog_postsPuzzles")

    def total_likespuzzles(self):
        return self.likes.count()

    def __str__(self):
        return f"{self.title} {self.date} {self.author}"

class CommentGames(models.Model):
    post = models.ForeignKey(PostGames,related_name="commentsGames",on_delete=models.CASCADE)
    commenter = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    date = models.DateTimeField(default=now, editable=False)
    
    def __str__(self):
        return f"{self.post.title} {self.commenter} {self.date}"

class CommentBio(models.Model):
    post = models.ForeignKey(PostBio,related_name="commentsBio",on_delete=models.CASCADE)
    commenter = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    date = models.DateTimeField(default=now, editable=False)
    
    def __str__(self):
        return f"{self.post.title} {self.commenter} {self.date}"

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='avatars', null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} {self.image.url}"