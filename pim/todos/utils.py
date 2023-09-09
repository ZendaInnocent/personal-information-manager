from django.db.models import Max


def get_order_value(user):
    user_todos = user.todos.all()

    if not user_todos.exists():
        return 1
    else:
        current_max = user_todos.aggregate(max_order=Max('order'))['max_order']
        return current_max + 1


def reorder(user):
    user_todos = user.todos.all()

    if not user_todos.exists():
        return

    number_of_todos = user_todos.count()
    new_ordering = range(1, number_of_todos + 1)

    new_todos = []

    for order, todo in zip(new_ordering, user_todos):
        todo.order = order
        new_todos.append(todo)

    user.todos.bulk_update(new_todos, fields=['order'])
