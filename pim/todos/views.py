from datastar_py.django import ServerSentEventGenerator as SSE
from datastar_py.django import datastar_response, read_signals
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.template.response import TemplateResponse
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
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
def todo_create_view(request):
    if request.method == 'POST':
        form = TodoForm(data=request.POST, initial={'user': request.user})

        if form.is_valid():
            form.save()
            messages.success(request, 'Todo created successful.')
            return redirect('todos:todo-index')
    else:
        form = TodoForm(initial={'user': request.user})

    return render(request, 'todos/todo_form.html', {'form': form})


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
@require_http_methods(['POST'])
def todo_delete_view(request, id):
    todo = request.user.todos.get(id=id)
    todo.delete()
    messages.success(request, 'Todo deleted successful.')
    return redirect('todos:todo-index')


@login_required
@require_http_methods(['POST'])
@csrf_exempt
@datastar_response
def todo_toggle_view(request, id: int):
    todo: Todo = request.user.todos.get(id=id)
    todo.toggle_completed()

    yield SSE.patch_elements(
        render_to_string('todos/partials/checkbox.html', {'todo': todo})
    )


@login_required
@csrf_exempt
@datastar_response
def sort_todos(request):
    signals = read_signals(request)
    user = request.user
    current_todos_order = signals.get('order')
    print(current_todos_order)

    new_ordered_todos = []

    for index, todo_pk in enumerate(current_todos_order, start=1):
        todo: Todo = request.user.todos.get(pk=todo_pk)
        todo.order = index
        new_ordered_todos.append(todo)

    user.todos.bulk_update(new_ordered_todos, fields=['order'])

    yield SSE.patch_elements(
        render_to_string('todos/partials/todo_list.html', {'todos': user.todos.all()})
    )
