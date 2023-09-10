from django.contrib import messages
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, QueryDict
from django.template.response import TemplateResponse

from .models import Todo


@login_required
def index(request: HttpRequest) -> TemplateResponse:
    if request.method == 'POST':
        text: str | None = request.POST.get('text', None)
        if text is None:
            return
        request.user.todos.create(text=text)
        messages.success(request, 'Task added succesful.')
        return TemplateResponse(
            request,
            'todos/partials/list.html',
            {
                'todos': request.user.todos.all(),
            },
        )

    return TemplateResponse(
        request,
        'todos/index.html',
        {
            'todos': request.user.todos.all(),
        },
    )


@login_required
def delete_todo(request: HttpRequest, id: int) -> TemplateResponse:
    request.user.todos.get(id=id).delete()
    return TemplateResponse(
        request,
        'todos/partials/list.html',
        {
            'todos': request.user.todos.all(),
        },
    )


@login_required
def toggle_todo(request: HttpRequest, id: int) -> TemplateResponse | None:
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


@login_required
def update_todo(request, id) -> TemplateResponse:
    todo: Todo = request.user.todos.get(id=id)

    if request.method == 'PUT':
        data = QueryDict(request.body)
        todo.text = data.get('text')
        todo.save()
        messages.success(request, 'Todo updated successful.')
        return TemplateResponse(request, 'todos/partials/todo.html', {'todo': todo})
