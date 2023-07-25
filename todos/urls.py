from django.urls import path
from . import views

app_name = 'todos'

urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<int:id>', views.delete, name='delete-todo'),
    path('toggle/<int:id>', views.toggle_todo, name='toggle-todo'),
]
