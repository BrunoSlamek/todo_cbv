from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import ToDo


class IndexView(ListView):
    model = ToDo
    template_name = 'index.html'
    queryset = ToDo.objects.all()
    context_object_name = 'todos'


class CreateTodo(CreateView):
    model = ToDo
    template_name = 'todo_form.html'
    fields = ['title', 'description', 'priority', 'is_active']
    success_url = reverse_lazy('index')


class UpdateToDo(UpdateView):
    model = ToDo
    template_name = 'todo_form.html'
    fields = ['title', 'description', 'priority', 'is_active']
    success_url = reverse_lazy('index')


class DeleteToDo(DeleteView):
    model = ToDo
    template_name = 'todo_del.html'
    success_url = reverse_lazy('index')
