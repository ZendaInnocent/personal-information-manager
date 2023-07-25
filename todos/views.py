from django.shortcuts import render

def index(request):
    template_name = 'todos/index.html'
    context = {}
    return render(request, template_name, context)