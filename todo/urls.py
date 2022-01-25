from django.urls import path
from .views import *


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('add/', CreateTodo.as_view(), name='add_todo'),
    path('<int:pk>', UpdateToDo.as_view(), name='upd_todo'),
    path('<int:pk>/delete/', DeleteToDo.as_view(), name='del_todo'),
]
