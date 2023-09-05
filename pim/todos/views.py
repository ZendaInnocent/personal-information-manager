from typing import Any

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, QueryDict
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from . import forms
from .models import Todo, UserTodo
from .utils import reorder


class TodoCreateView(CreateView):
    model = Todo
    form_class = forms.TodoForm
    success_url = reverse_lazy('todos:todos-index')

    def get_initial(self) -> dict[str, Any]:
        return {'user': self.request.user}


create_todo = TodoCreateView.as_view()


@login_required
def index(request) -> HttpResponse:
    template_name = 'todos/index.html'
    user_todos = UserTodo.objects.prefetched_user_todo().filter(user=request.user)

    context = {
        'user_todos': user_todos,
        'form': forms.TodoForm(),
    }
    return render(request, template_name, context)


@login_required
def delete_todo(request, id) -> HttpResponse:
    todo = Todo.objects.prefetched_user().filter(user=request.user).get(id=id)

    if todo.user == request.user:
        user_todo = (
            UserTodo.objects.prefetched_user_todo()
            .filter(user=request.user)
            .get(todo=todo)
        )
        user_todo.delete()
        reorder(request.user)
        messages.success(request, 'Todo deleted successful.')

    user_todos = UserTodo.objects.prefetched_user_todo().filter(user=request.user)

    context = {
        'user_todos': user_todos,
    }
    return render(request, 'todos/partials/list.html', context)


@login_required
def toggle_todo(request, id) -> HttpResponse | None:
    template_name = 'todos/partials/checkbox.html'

    if request.method == 'POST':
        todo = Todo.objects.prefetched_user().filter(user=request.user).get(id=id)

        if todo.user == request.user:
            todo.is_completed = not todo.is_completed
            todo.save()

        user_todo = UserTodo.objects.prefetched_user_todo().get(
            user=request.user, todo=todo
        )
        return render(request, template_name, {'todo': user_todo.todo})


@login_required
def update_todo(request, id) -> HttpResponse:
    todo = Todo.objects.prefetched_user().get(id=id)

    if request.method == 'PUT':
        data = QueryDict(request.body)
        if todo.user == request.user:
            todo.text = data.get('todo')
            todo.save()
            messages.success(request, 'Todo updated successful.')
            return HttpResponse(status=204)
        else:
            messages.error(request, 'You are not have access to update this todo.')

        user_todo = (
            UserTodo.objects.prefetched_user_todo()
            .filter(user=request.user)
            .get(todo=todo)
        )
        return render(request, 'todos/partials/todo.html', {'user_todo': user_todo})

    context = {'todo': todo}
    return render(request, 'todos/partials/form.html', context)


@login_required
def sort_todos(request) -> HttpResponse:
    current_todos_order = request.POST.getlist('user_todo')

    new_ordered_user_todos = []

    for index, user_todo_pk in enumerate(current_todos_order, start=1):
        user_todo = (
            UserTodo.objects.prefetched_user_todo()
            .filter(user=request.user)
            .get(pk=user_todo_pk)
        )
        user_todo.order = index
        new_ordered_user_todos.append(user_todo)

    UserTodo.objects.bulk_update(new_ordered_user_todos, fields=['order'])

    user_todos = UserTodo.objects.prefetched_user_todo().filter(user=request.user)

    template_name = 'todos/partials/list.html'
    context = {'user_todos': user_todos}
    return render(request, template_name, context)
