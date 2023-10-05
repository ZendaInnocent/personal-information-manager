from django.contrib import messages
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import redirect
from django.template.response import TemplateResponse
from django.urls import reverse_lazy

from .forms import TodoForm
from .models import Todo


@login_required
def todo_list(request: HttpRequest) -> TemplateResponse:
    todos: [Todo] = request.user.todos.all()
    return TemplateResponse(request, 'todos/todo_list.html', {'todos': todos})


@login_required
def todo_add(request: HttpRequest) -> TemplateResponse:
    form: TodoForm = TodoForm(initial={'user': request.user})

    if request.method == 'POST':
        form = TodoForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Task added successful.')
            return redirect(reverse_lazy('todos:todo-list'))
        else:
            form = TodoForm(request.POST)
    return TemplateResponse(request, 'todos/todo_form.html', {'form': form})


@login_required
def todo_update(request, id) -> TemplateResponse:
    todo: Todo = request.user.todos.get(id=id)
    form = TodoForm(instance=todo)

    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)

        if form.is_valid():
            form.save()
            messages.success(request, 'Task updated successful.')
            return redirect(reverse_lazy('todos:todo-list'))

    return TemplateResponse(request, 'todos/todo_form.html', {'form': form})


@login_required
def todo_delete(request: HttpRequest, id: int) -> HttpResponseRedirect:
    request.user.todos.get(id=id).delete()
    messages.success(request, 'Task deleted successful.')
    return HttpResponseRedirect(reverse_lazy('todos:todo-list'))


@login_required
def todo_toggle(request: HttpRequest, id: int) -> TemplateResponse | None:
    if request.method == 'POST':
        todo: Todo = request.user.todos.get(id=id)
        todo.toggle_completed()
        return TemplateResponse(
            request,
            'todos/partials/checkbox.html',
            {
                'todo': todo,
            },
        )


@login_required
def sort_todos(request: HttpRequest) -> TemplateResponse:
    user: AbstractBaseUser = request.user
    current_todos_order = request.POST.getlist('todo')

    new_ordered_todos = []

    for index, todo_pk in enumerate(current_todos_order, start=1):
        todo: Todo = (
            Todo.objects.select_related('user')
            .filter(user=request.user)
            .get(pk=todo_pk)
        )
        todo.order = index
        new_ordered_todos.append(todo)

    user.todos.bulk_update(new_ordered_todos, fields=['order'])

    return TemplateResponse(
        request,
        'todos/partials/list.html',
        {
            'todos': user.todos.all(),
        },
    )
