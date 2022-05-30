from django.shortcuts import redirect, render, get_list_or_404
from django.urls import reverse_lazy, reverse
from .models import Message
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

# Create your views here.

@login_required
def PeopleWeCanMessage(request):
    people = User.objects.all()
    context = {'people':people}
    return render(request, 'Direct/can_message_list.html', context)


class NewMessage(LoginRequiredMixin,CreateView):
    model = Message
    fields = ['body']   
    def form_valid(self,form):
        form.instance.sender=self.request.user
        form.instance.recipient = User.objects.get(id=self.kwargs['pk'])
        form.save()
        return super().form_valid(form)
    def get_success_url(self) -> str:
        messages.success(self.request, ('Mensaje enviado con éxito!'))
        return reverse_lazy('Index')

@login_required
def Inbox(request):
    messages = Message.objects.filter(recipient_id=request.user).order_by('-date')
    context = {'messages':messages}
    return render(request, 'Direct/inbox.html', context)

