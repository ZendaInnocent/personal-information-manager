import pytest
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractBaseUser

from ..models import Todo


@pytest.fixture()
def testuser() -> AbstractBaseUser:
    return get_user_model().objects.create(username='username')


def test_todo_string_method(testuser) -> None:
    todo: Todo = Todo.objects.create(user=testuser, text='some text')

    assert str(todo) == todo.text


def test_todo_manager_prefetched_user(testuser) -> None:
    _todos: list[Todo] = [
        Todo.objects.create(user=testuser, text='some text') for i in range(5)
    ]

    todos: list[Todo] = (
        Todo.objects.prefetched_user().filter(user=testuser).order_by('created_at')
    )

    assert list(todos) == _todos
