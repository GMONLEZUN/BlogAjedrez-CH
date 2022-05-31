from django.contrib import admin

# Register your models here.
from Posts.models import PostBio,PostGames,PostPuzzles,CommentGames,CommentBio, Avatar

admin.site.register(PostBio)
admin.site.register(PostGames)
admin.site.register(PostPuzzles)
admin.site.register(CommentGames)
admin.site.register(CommentBio)
admin.site.register(Avatar)
