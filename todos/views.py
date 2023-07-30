from django.shortcuts import render
from django.contrib import messages
from django.http import QueryDict
from django.contrib.auth.decorators import login_required

from .models import Todo, UserTodo
from .utils import get_order_value, reorder


def test_user(user, todo):
    return user == todo.user

@login_required
def index(request):

    if request.method == 'POST':
        text = request.POST.get('todo')
        todo = Todo.objects.create(text=text, user=request.user)
        todo.usertodo_set.create(
            user=request.user, order=get_order_value(request.user))

        user_todos = UserTodo.objects.filter(user=request.user)

        context = {
            'user_todos': user_todos,
        }
        return render(request, 'todos/partials/list.html', context)


    template_name = 'todos/index.html'
    user_todos = UserTodo.objects.filter(user=request.user)

    context = {
        'user_todos': user_todos
    }
    return render(request, template_name, context)


def delete(request, id):
    todo = Todo.objects.get(id=id)

    if todo.user == request.user:
        user_todo = UserTodo.objects.get(user=request.user, todo=todo)
        user_todo.delete()
        reorder(request.user)
        messages.success(request, 'Todo deleted successful.')

    user_todos = UserTodo.objects.filter(user=request.user)

    context = {
        'user_todos': user_todos,
    }
    return render(request, 'todos/partials/list.html', context)


def toggle_todo(request, id):
    template_name = 'todos/partials/checkbox.html'

    if request.method == 'POST':
        todo = Todo.objects.get(id=id)

        if todo.user == request.user:
            todo.is_completed = not todo.is_completed
            todo.save()

        user_todo = UserTodo.objects.get(user=request.user, todo=todo)
        return render(request, template_name, {'todo': user_todo.todo})


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

        user_todo = UserTodo.objects.get(todo=todo, user=request.user)
        return render(request, 'todos/partials/todo.html', {'user_todo': user_todo})

    context = {'todo': todo}
    return render(request, 'todos/partials/form.html', context)


def sort_todos(request):
    current_todos_order = request.POST.getlist('todo')

    for index, todo_pk in enumerate(current_todos_order, start=1):
        user_todo = UserTodo.objects.get(pk=todo_pk)
        user_todo.order = index
        user_todo.save()

    user_todos = UserTodo.objects.filter(user=request.user)

    template_name = 'todos/partials/list.html'
    context = {'user_todos': user_todos}
    return render(request, template_name, context)
