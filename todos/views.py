from django.shortcuts import render
from .models import Todo


def index(request):
    todos = Todo.objects.order_by('-id')

    if request.method == 'POST':
        text = request.POST.get('todo')
        Todo.objects.create(text=text)

    template_name = 'todos/index.html'
    context = {
        'todos': todos
    }
    return render(request, template_name, context)