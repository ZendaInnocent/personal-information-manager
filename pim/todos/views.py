from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.template.response import TemplateResponse

from .models import Todo


@login_required
def index(request: HttpRequest) -> TemplateResponse:
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
        todo.is_completed = not todo.is_completed
        todo.save()
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
        todo: Todo = user.todos.get(pk=todo_pk)
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


# @login_required
# def update_todo(request, id) -> HttpResponse:
#     todo = Todo.objects.prefetched_user().get(id=id)

#     if request.method == 'PUT':
#         data = QueryDict(request.body)
#         if todo.user == request.user:
#             todo.text = data.get('todo')
#             todo.save()
#             messages.success(request, 'Todo updated successful.')
#             return HttpResponse(status=204)
#         else:
#             messages.error(request, 'You are not have access to update this todo.')

#         user_todo = (
#             UserTodo.objects.prefetched_user_todo()
#             .filter(user=request.user)
#             .get(todo=todo)
#         )
#         return render(request, 'todos/partials/todo.html', {'user_todo': user_todo})

#     context = {'todo': todo}
#     return render(request, 'todos/partials/form.html', context)
