from django.shortcuts import render
from django.contrib import messages
from django.http import QueryDict

from .models import Todo


def index(request):
    if request.method == 'POST':
        text = request.POST.get('todo')
        todo = Todo.objects.create(text=text)
        return render(request, 'todos/partials/todo.html', {'todo': todo})
    
    todos = Todo.objects.all()
    
    template_name = 'todos/index.html'
    context = {
        'todos': todos
    }
    return render(request, template_name, context)


def delete(request, id):
    Todo.objects.get(id=id).delete()
    messages.success(request, 'Todo deleted successful.')

    context = {
        'todos': Todo.objects.all(),
    }
    return render(request, 'todos/partials/list.html', context)


def toggle_todo(request, id):
    template_name = 'todos/partials/checkbox.html'
    if request.method == 'POST':
        todo = Todo.objects.get(id=id)
        todo.is_completed = not todo.is_completed
        todo.save()
        return render(request, template_name, {'todo': todo})


def update(request, id):
    # messages.success(request, 'Todo edited successful.')
    todo = Todo.objects.get(id=id)
    if request.method == 'PUT':
        data = QueryDict(request.body)
        todo.text = data['todo']
        todo.save()
        messages.success(request, 'Todo edited successful.')
        return render(request, 'todos/partials/todo.html', {todo: todo.refresh_from_db()})
    return render(request, 'todos/partials/form.html', {'todo': todo})
