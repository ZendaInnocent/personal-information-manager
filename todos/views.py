from django.shortcuts import render
from django.contrib import messages
from django.http import QueryDict
from django.contrib.auth.decorators import login_required, user_passes_test

from .models import Todo

def test_user(user, todo):
    return user == todo.user

@login_required
def index(request):
    if request.method == 'POST':
        text = request.POST.get('todo')
        todo = Todo.objects.create(text=text, user=request.user)
        return render(request, 'todos/partials/todo.html', {'todo': todo})

    todos = Todo.objects.filter(user=request.user)

    template_name = 'todos/index.html'
    context = {
        'todos': todos
    }
    return render(request, template_name, context)


def delete(request, id):
    todo = Todo.objects.get(id=id)

    if todo.user == request.user:
        todo.delete()
        messages.success(request, 'Todo deleted successful.')

    context = {
        'todos': Todo.objects.filter(user=request.user),
    }
    return render(request, 'todos/partials/list.html', context)


def toggle_todo(request, id):
    template_name = 'todos/partials/checkbox.html'

    if request.method == 'POST':
        todo = Todo.objects.get(id=id)

        if todo.user == request.user:
            todo.is_completed = not todo.is_completed
            todo.save()
        return render(request, template_name, {'todo': todo})


def update_todo(request, id):
    todo = Todo.objects.get(id=id)

    if request.method == 'PUT':
        data = QueryDict(request.body)
        if todo.user == request.user:
            todo.text = data.get('todo')
            todo.save()
            messages.success(request, 'Todo updated successful.')
        else:
            messages.error(
                request, 'You are not have access to update this todo.')
        return render(request, 'todos/partials/todo.html', {'todo': todo})

    context = {'todo': todo}
    return render(request, 'todos/partials/form.html', context)
