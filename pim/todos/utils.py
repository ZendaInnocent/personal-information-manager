from django.db.models import Max

from .models import UserTodo


def get_order_value(user):
    existing_user_todos = UserTodo.objects.filter(user=user)

    if not existing_user_todos.exists():
        return 1
    else:
        current_max = existing_user_todos.aggregate(max_order=Max('order'))['max_order']
        return current_max + 1


def reorder(user):
    existing_user_todos = UserTodo.objects.prefetched_user_todo().filter(user=user)
    if not existing_user_todos.exists():
        return

    number_of_user_todos = existing_user_todos.count()
    new_ordering = range(1, number_of_user_todos + 1)

    new_user_todos = []

    for order, user_todo in zip(new_ordering, existing_user_todos):
        user_todo.order = order
        new_user_todos.append(user_todo)

    UserTodo.objects.bulk_update(new_user_todos, fields=['order'])
