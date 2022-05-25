from django.contrib import admin

# Register your models here.
from Posts.models import PostBio,PostGames

admin.site.register(PostBio)
admin.site.register(PostGames)