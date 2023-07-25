from django.shortcuts import render
from .models import Todo


def index(request):
    todos = Todo.objects.order_by('-id')

    if request.method == 'POST':
        text = request.POST.get('todo')
        todo = Todo.objects.create(text=text)
        return render(request, 'todos/todo.html', {'todo': todo})

    template_name = 'todos/index.html'
    context = {
        'todos': todos
    }
    return render(request, template_name, context)