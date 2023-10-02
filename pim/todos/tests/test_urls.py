from django.urls import resolve, reverse

from pim.todos import views


def test_todo_list_url_resolves() -> None:
    url = reverse('todos:todo-list')

    assert resolve(url).func == views.todo_list


def test_todo_add_url_resolves() -> None:
    url = reverse('todos:todo-add')

    assert resolve(url).func == views.todo_add


def test_todo_update_url_resolves() -> None:
    url = reverse('todos:todo-update', kwargs={'id': 1})

    assert resolve(url).func == views.todo_update


def test_todo_delete_url_resolves() -> None:
    url = reverse('todos:todo-delete', kwargs={'id': 1})

    assert resolve(url).func == views.todo_delete


def test_todo_toggle_url_resolves() -> None:
    url = reverse('todos:todo-toggle', kwargs={'id': 1})

    assert resolve(url).func == views.todo_toggle


def test_sort_todos_url_resolves() -> None:
    url = reverse('todos:sort-todos')

    assert resolve(url).func == views.sort_todos
