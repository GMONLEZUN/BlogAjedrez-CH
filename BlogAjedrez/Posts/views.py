from datetime import datetime
import http
from msilib.schema import Class
from django.http import HttpResponse
from django.shortcuts import render
from Posts.models import PostBio, PostGames, PostPuzzles
from datetime import datetime
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy

# Create your views here.

def index(request):
    return render (request, "Posts/index.html")

def puzzles(request):
    return render (request, "Posts/puzzles.html")      

# def biography(request):
#     return render (request, "Posts/biography.html")    

# def games(request):
#     return render (request, "Posts/games.html")    

def offTopic(request):
    return render (request, "Posts/offtopic.html")    

def about(request):
    return render (request, "Posts/about.html")    


# ------------------------------------------------------------------------------------------    BIOGRAPHY    ----------------------------------------


class BioList(ListView):
    model = PostBio
    template_name = "Posts/postbio_list.html"

class BioDetail(DetailView):
    model = PostBio
    template_name = "Posts/postbio_detail.html"

class BioCreation(CreateView):
    model = PostBio
    success_url = reverse_lazy('BioList')
    fields = ['title', 'content','image']

class BioUpdate(UpdateView):
    model = PostBio
    success_url = reverse_lazy('BioList')
    fields = ['title', 'content','image']

class BioDelete(DeleteView):
    model = PostBio
    success_url = reverse_lazy('BioList')



# ------------------------------------------------------------------------------------------    SEARCH    ----------------------------------------

def searchPost(request):
    if request.GET['title']:
        title = request.GET['apellido']
        posts = PostBio.objects.filter(title__icontains = title)
        return render(request, "Posts/resultadoBusqueda.html",{'posts':posts})
    else:
        respuesta = "No enviaste datos"
        return HttpResponse(respuesta)



# ------------------------------------------------------------------------------------------    GAMES    ----------------------------------------

class GamesList(ListView):
    model = PostGames
    template_name = "Posts/postgames_list.html"

class GamesDetail(DetailView):
    model = PostGames
    template_name = "Posts/postgames_detail.html"

class GamesCreation(CreateView):
    model = PostGames
    success_url = reverse_lazy('GamesList')
    fields = ['title','title_players', 'result', 'content','image']

class GamesUpdate(UpdateView):
    model = PostGames
    success_url = reverse_lazy('GamesList')
    fields = ['title','title_players', 'result', 'content','image']

class GamesDelete(DeleteView):
    model = PostGames
    success_url = reverse_lazy('GamesList')

# ------------------------------------------------------------------------------------------    PUZZLES    ----------------------------------------


class PuzzlesList(ListView):
    model = PostPuzzles
    template_name = "Posts/postpuzzles_list.html"

class PuzzlesDetail(DetailView):
    model = PostPuzzles
    template_name = "Posts/postpuzzles_detail.html"

class PuzzlesCreation(CreateView):
    model = PostPuzzles
    success_url = reverse_lazy('PuzzlesList')
    fields = ['title','solution','content','image']

class PuzzlesUpdate(UpdateView):
    model = PostPuzzles
    success_url = reverse_lazy('PuzzlesList')
    fields = ['title','solution','content','image']

class PuzzlesDelete(DeleteView):
    model = PostPuzzles
    success_url = reverse_lazy('PuzzlesList')