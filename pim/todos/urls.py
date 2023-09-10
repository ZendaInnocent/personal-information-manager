from django.urls import path

from . import views

app_name = 'todos'

urlpatterns = [
    path('', views.index, name='todos-index'),
    path('update/<int:id>', views.update_todo, name='update-todo'),
    path('delete/<int:id>', views.delete_todo, name='delete-todo'),
    path('toggle/<int:id>', views.toggle_todo, name='toggle-todo'),
    path('sort/', views.sort_todos, name='sort-todos'),
]
