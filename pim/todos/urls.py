from django.urls import path

from . import views

app_name = 'todos'

urlpatterns = [
    path('', views.index, name='todo-index'),
    path('create/', views.todo_create_view, name='todo-create'),
    path('update/<int:id>', views.todo_update, name='todo-update'),
    path('delete/<int:id>', views.todo_delete, name='todo-delete'),
    path('toggle/<int:id>', views.todo_toggle_view, name='todo-toggle'),
    path('sort/', views.sort_todos, name='sort-todos'),
]
