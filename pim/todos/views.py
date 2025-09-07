from datastar_py import consts
from datastar_py.django import ServerSentEventGenerator as SSE
from datastar_py.django import datastar_response
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.template.response import TemplateResponse
from django.urls import reverse_lazy
from django.views.decorators.http import require_http_methods

from .forms import TodoForm
from .models import Todo


@login_required
def index(request):
    context = {
        'todos': request.user.todos.all(),
        'form': TodoForm(initial={'user': request.user}),
    }
    return render(request, 'todos/index.html', context)


@login_required
@require_http_methods(['POST'])
@datastar_response
def todo_create(request):
    form = TodoForm(initial={'user': request.user}, data=request.POST)

    if form.is_valid():
        todo = form.save()
        messages.success(request, f"Task '{todo.text}' added successful.")
        yield SSE.patch_elements(
            render_to_string('todos/partials/todo_item.html', {'todo': todo}),
            '#todos-list form',
            mode=consts.ElementPatchMode.APPEND,
        )


@login_required
def todo_update(request, id):
    todo: Todo = request.user.todos.get(id=id)
    form = TodoForm(instance=todo)

    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)

        if form.is_valid():
            form.save()
            messages.success(request, 'Task updated successful.')
            return redirect(reverse_lazy('todos:todo-index'))

    return TemplateResponse(
        request, 'todos/todo_form.html', {'title': 'Update', 'form': form}
    )


@login_required
def todo_delete(request: HttpRequest, id: int):
    if request.method == 'POST':
        request.user.todos.get(id=id).delete()
        messages.success(request, 'Task deleted successful.')
        return TemplateResponse(
            request,
            'todos/partials/list.html',
            {'todos': request.user.todos.all()},
        )


@login_required
def todo_toggle(request: HttpRequest, id: int):
    if request.method == 'POST':
        todo: Todo = request.user.todos.get(id=id)
        todo.toggle_completed()
        return TemplateResponse(
            request,
            'todos/partials/checkbox.html',
            {'todo': todo},
        )


@login_required
def sort_todos(request):
    user = request.user
    current_todos_order = request.POST.getlist('todo')

    new_ordered_todos = []

    for index, todo_pk in enumerate(current_todos_order, start=1):
        todo: Todo = request.user.todos.get(pk=todo_pk)
        todo.order = index
        new_ordered_todos.append(todo)

    user.todos.bulk_update(new_ordered_todos, fields=['order'])

    return TemplateResponse(
        request,
        'todos/partials/todo_list.html',
        {'todos': user.todos.all()},
    )
