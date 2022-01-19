from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import ToDo

"""
def index(request):
    return render(request, 'index.html')
"""


class IndexView(ListView):
    models = ToDo
    template_name = 'index.html'
    queryset = ToDo.objects.all()
    context_object_name = 'todos'
