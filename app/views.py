from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, FormView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from .models import Task

class Login(LoginView):
    template_name = 'app/login.html'
    fields = '__all__'
    redirect_authenticated_user =True
    
    def get_success_url(self) -> str:
        return reverse_lazy('todos')
    
class RegisterPage(FormView):
    template_name = 'app/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('todos')

    def form_valid(self, form):
        user = form.save()
        if user :
            login(self.request, user)
        return super().form_valid(form)
    
    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('todos')
        return super().get(request, *args, **kwargs)


class TodoList( LoginRequiredMixin, ListView ):
    model = Task
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user = self.request.user)
        return context


class AddTask(LoginRequiredMixin, CreateView):
    model = Task
    fields = [ 'title', 'desc', 'isComplete' ]
    success_url = reverse_lazy('todos')

    def form_valid(self, form):
        form.instance.user = self.request.user
        print(form.instance)
        return super().form_valid(form)

class DeleteTask(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('todos')
