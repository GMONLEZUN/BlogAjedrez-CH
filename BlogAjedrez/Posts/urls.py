from django import views
from django.urls import path
from Posts.views import index, about, login_request,register,GamesList,GamesDetail,GamesCreation,GamesUpdate,GamesDelete, BioCreation,BioDelete,BioDetail,BioList,BioUpdate, PuzzlesCreation,PuzzlesDelete,PuzzlesDetail,PuzzlesUpdate, PuzzlesList
from django.contrib.auth.views import LogoutView



urlpatterns = [

    path('', index, name="Index"),
    path('about/', about, name="About"),
    path('login/', login_request, name="Login"),
    path('register/', register, name="Register"),
    path('logout/', LogoutView.as_view(template_name='Posts/index.html'), name="Logout"),

    path('games/list/', GamesList.as_view(), name="GamesList"),
    path('games/<pk>', GamesDetail.as_view(), name="GamesDetail"),
    path('games/new/', GamesCreation.as_view(), name="GamesCreation"),
    path('games/edit/<pk>', GamesUpdate.as_view(), name="GamesUpdate"),
    path('games/delete/<pk>', GamesDelete.as_view(), name="GamesDelete"),

    path('biography/list/', BioList.as_view(), name="BioList"),
    path('biography/<pk>', BioDetail.as_view(), name="BioDetail"),
    path('biography/new/', BioCreation.as_view(), name="BioCreation"),
    path('biography/edit/<pk>', BioUpdate.as_view(), name="BioUpdate"),
    path('biography/delete/<pk>', BioDelete.as_view(), name="BioDelete"),

    path('puzzles/list/', PuzzlesList.as_view(), name="PuzzlesList"),
    path('puzzles/<pk>', PuzzlesDetail.as_view(), name="PuzzlesDetail"),
    path('puzzles/new/', PuzzlesCreation.as_view(), name="PuzzlesCreation"),
    path('puzzles/edit/<pk>', PuzzlesUpdate.as_view(), name="PuzzlesUpdate"),
    path('puzzles/delete/<pk>', PuzzlesDelete.as_view(), name="PuzzlesDelete"),
]

