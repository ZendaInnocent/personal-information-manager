from django.urls import path

from . import views

app_name = 'todos'

urlpatterns = [
    path('', views.todo_list, name='todo-list'),
    path('add/', views.todo_add, name='todo-add'),
    path('update/<int:id>', views.todo_update, name='todo-update'),
    path('delete/<int:id>', views.todo_delete, name='todo-delete'),
    path('toggle/<int:id>', views.todo_toggle, name='todo-toggle'),
    path('sort/', views.sort_todos, name='sort-todos'),
]
