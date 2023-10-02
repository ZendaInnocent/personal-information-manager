from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, QueryDict
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
            return redirect(reverse_lazy('todos:todo-list'))
        else:
            form = TodoForm(request.POST)
    return TemplateResponse(request, 'todos/todo_form.html', {'form': form})


@login_required
def todo_update(request, id) -> TemplateResponse:
    todo: Todo = request.user.todos.get(id=id)

    if request.method == 'PUT':
        data = QueryDict(request.body)
        todo.text = data.get('text')
        todo.save()
        return TemplateResponse(request, 'todos/partials/todo.html', {'todo': todo})


@login_required
def todo_delete(request: HttpRequest, id: int) -> TemplateResponse:
    request.user.todos.get(id=id).delete()
    return TemplateResponse(
        request,
        'todos/partials/list.html',
        {
            'todos': request.user.todos.all(),
        },
    )


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
        todo: Todo = user.todos.prefetch_related('todo').get(pk=todo_pk)
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
