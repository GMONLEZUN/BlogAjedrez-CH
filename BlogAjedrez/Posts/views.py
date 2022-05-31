
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from Posts.forms import UserRegistrationForm,UserLoginForm, UserEditForm, AvatarForm
from Posts.models import Avatar, PostBio, PostGames, PostPuzzles,CommentGames,CommentBio
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash

# Create your views here.

def index(request):
    return render (request, "Posts/index.html")

def about(request):
    return render (request, "Posts/about.html")    


# ------------------------------------------------------------------------------------------    BIOGRAPHY    ----------------------------------------


class BioList(ListView):
    model = PostBio
    template_name = "Posts/postbio_list.html"
    queryset = PostBio.objects.order_by('-id')

class BioDetail(DetailView):
    model = PostBio
    template_name = "Posts/postbio_detail.html"

    def get_context_data(self, *args,**kwargs):
        context = super(BioDetail,self).get_context_data(**kwargs)
        idpost = get_object_or_404(PostBio, id=self.kwargs['pk'])
        total_likesbio = idpost.total_likesbio()
        context["total_likesbio"] = total_likesbio
        return context

class BioCreation(LoginRequiredMixin,CreateView):
    model = PostBio
    success_url = reverse_lazy('BioList')
    fields = ['title', 'content','image']
    def form_valid(self,form):
        form.instance.author=self.request.user
        messages.success(self.request, "Post creado con éxito!")
        return super().form_valid(form)

class BioUpdate(LoginRequiredMixin,UpdateView):
    model = PostBio
    success_url = reverse_lazy('BioList')
    fields = ['title', 'content','image']
    def form_valid(self, form):
      messages.success(self.request, "Post editado con éxito!")
      return super().form_valid(form)

class BioDelete(LoginRequiredMixin,DeleteView):
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
    queryset = PostGames.objects.order_by('-id')

class GamesDetail(DetailView):
    model = PostGames
    template_name = "Posts/postgames_detail.html"
    
    def get_context_data(self, *args,**kwargs):
        context = super(GamesDetail,self).get_context_data(**kwargs)
        idpost = get_object_or_404(PostGames, id=self.kwargs['pk'])
        total_likesgames = idpost.total_likesgames()
        context["total_likesgames"] = total_likesgames
        return context

class GamesCreation(LoginRequiredMixin,CreateView):
    model = PostGames
    success_url = reverse_lazy('GamesList')
    fields = ['title','title_players','result', 'content','image']
    def form_valid(self,form):
        form.instance.author=self.request.user
        messages.success(self.request, "Post creado con éxito!")
        return super().form_valid(form)
   

class GamesUpdate(LoginRequiredMixin,UpdateView):
    model = PostGames
    success_url = reverse_lazy('GamesList')
    fields = ['title','title_players', 'result', 'content','image']
    def form_valid(self, form):
      messages.success(self.request, "Post editado con éxito!")
      return super().form_valid(form)


class GamesDelete(LoginRequiredMixin,DeleteView):
    model = PostGames
    success_url = reverse_lazy('GamesList')

# ------------------------------------------------------------------------------------------    PUZZLES    ----------------------------------------


class PuzzlesList(ListView):
    model = PostPuzzles
    template_name = "Posts/postpuzzles_list.html"
    queryset = PostPuzzles.objects.order_by('-id')

class PuzzlesDetail(DetailView):
    model = PostPuzzles
    template_name = "Posts/postpuzzles_detail.html"

    def get_context_data(self, *args,**kwargs):
        context = super(PuzzlesDetail,self).get_context_data(**kwargs)
        idpost = get_object_or_404(PostPuzzles, id=self.kwargs['pk'])
        total_likespuzzles = idpost.total_likespuzzles()
        context["total_likespuzzles"] = total_likespuzzles
        return context


class PuzzlesCreation(LoginRequiredMixin,CreateView):
    model = PostPuzzles
    success_url = reverse_lazy('PuzzlesList')
    fields = ['title','solution','content','image']
    def form_valid(self,form):
        form.instance.author=self.request.user
        messages.success(self.request, "Post creado con éxito!")
        return super().form_valid(form)

class PuzzlesUpdate(LoginRequiredMixin,UpdateView):
    model = PostPuzzles
    success_url = reverse_lazy('PuzzlesList')
    fields = ['title','solution','content','image']
    def form_valid(self, form):
      messages.success(self.request, "Post editado con éxito!")
      return super().form_valid(form)

class PuzzlesDelete(LoginRequiredMixin,DeleteView):
    model = PostPuzzles
    success_url = reverse_lazy('PuzzlesList')
    


# ------------------------------------------------------------------------------------------    LOGIN    ----------------------------------------

def login_request(request):
    if request.method == 'POST':
        form = UserLoginForm(request = request, data = request.POST)
        if form.is_valid():
            user = form.cleaned_data.get('username')
            passwd = form.cleaned_data.get('password')

            userName = authenticate(username=user, password=passwd)

            if userName is not None:
                login(request,userName)
                return render(request,'Posts/index.html',{"user":user}) 
            else:
                mensaje = "El usuario o la contraseña son incorrectos"
                return render(request,'Posts/login.html',{"mensaje":mensaje, "form":form})

        else:
            mensaje = "El usuario o la contraseña son incorrectos"
            return render(request,'Posts/login.html',{"mensaje":mensaje, "form":form})

    else:
        form = UserLoginForm()
        return render(request,'Posts/login.html',{"form":form})


# ------------------------------------------------------------------------------------------    REGISTRO    ----------------------------------------

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            messages.success(request, ('Usuario registrado exitosamente!'))
            return render(request,'Posts/index.html')
            # else caso error
    else:
        form = UserRegistrationForm()
    return render(request,'Posts/registro.html',{'form':form})

# ------------------------------------------------------------------------------------------    comments    ----------------------------------------

class CommentsGameCreation(LoginRequiredMixin,CreateView):
    model = CommentGames
    fields = ['body']   
    def form_valid(self,form):
        form.instance.commenter=self.request.user
        form.instance.post_id = self.kwargs['pk']
        form.save()
        return super().form_valid(form)
    def get_success_url(self) -> str:
        return reverse_lazy('GamesDetail', kwargs={'pk': self.object.post.id})


class CommentsBioCreation(LoginRequiredMixin,CreateView):
    model = CommentBio
    fields = ['body']
    def form_valid(self,form):
        form.instance.commenter=self.request.user
        form.instance.post_id = self.kwargs['pk']
        form.save()
        return super().form_valid(form)
    def get_success_url(self) -> str:
        return reverse_lazy('BioDetail', kwargs={'pk': self.object.post.id})

class CommentsBioDelete(LoginRequiredMixin,DeleteView):
    model = CommentBio
    def get_success_url(self) -> str:
        return reverse_lazy('BioDetail', kwargs={'pk': self.object.post.id})
        
class CommentsGamesDelete(LoginRequiredMixin,DeleteView):
    model = CommentGames
    def get_success_url(self) -> str:
        return reverse_lazy('GamesDetail', kwargs={'pk': self.object.post.id})


def like_postgames(request, pk):
    postgames = get_object_or_404(PostGames, id=request.POST.get('postgames_id'))
    postgames.likes.add(request.user)
    return HttpResponseRedirect(reverse('GamesDetail', args=[str(pk)]))

def like_biography(request, pk):
    postbio = get_object_or_404(PostBio, id=request.POST.get('postbio_id'))
    postbio.likes.add(request.user)
    return HttpResponseRedirect(reverse('BioDetail', args=[str(pk)]))

def like_puzzles(request, pk):
    postpuzzles = get_object_or_404(PostPuzzles, id=request.POST.get('postpuzzles_id'))
    postpuzzles.likes.add(request.user)
    return HttpResponseRedirect(reverse('PuzzlesDetail', args=[str(pk)]))


# ------------------------------------------------------------------------------------------    search    ----------------------------------------

def Search(request):
    if request.GET["input-busqueda"]:
        input = request.GET["input-busqueda"]
        bio = PostBio.objects.filter(title__icontains=input)
        games = PostGames.objects.filter(title__icontains=input)
        puzzles = PostPuzzles.objects.filter(title__icontains=input)
        
        return render(request,"Posts/search.html", {"bio":bio,"games":games,"puzzles":puzzles})

    else:
        respuesta = "No enviaste datos"
        return render(request,"Posts/search.html", {"respuesta":respuesta})

# ------------------------------------------------------------------------------------------    editar perfil    ----------------------------------------
@login_required
def EditProfile(request):
    user=request.user
    avatar = Avatar.objects.filter(user=request.user.id)
    if request.method == 'POST':
        form=UserEditForm(request.POST, instance=user)
        if form.is_valid():
            info=form.cleaned_data
            user.email=info['email']
            user.set_password(info['password1'])
            user.save()
            update_session_auth_hash(request, user)
            return render(request, 'Posts/index.html')
    else:
        form=UserEditForm(instance=user)
        if avatar:
            avatar_url=avatar[0].image.url
            return render(request, 'Posts/edit_profile.html', {'form':form, 'user':user.username, "image":avatar_url})
    return render(request, 'Posts/edit_profile.html', {'form':form, 'user':user.username})


@login_required
def ModifyAvatar(request):
    user = User.objects.get(username = request.user)
    if request.method == 'POST':
        formAvatar = AvatarForm(request.POST, request.FILES)
        if formAvatar.is_valid():
            avatarOld = Avatar.objects.filter(user=request.user)
            if(avatarOld):
                avatarOld.delete()
            avatar = Avatar(user=user,image=formAvatar.cleaned_data['image'])
            avatar.save()
            messages.success(request, ('Avatar modificado exitosamente!'))
            return render(request, 'Posts/index.html', {'user':user})
    else:
        formAvatar = AvatarForm()
    return render(request, 'Posts/edit_avatar.html',{'formAvatar':formAvatar,'user':user})