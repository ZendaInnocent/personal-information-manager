import pytest
from django.contrib.auth.models import AbstractBaseUser
from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.urls import reverse, reverse_lazy
from pytest_django.asserts import assertTemplateUsed

from pim.accounts.tests.factories import UserFactory

from ..forms import TodoForm
from ..models import Todo


@pytest.fixture()
def testuser() -> AbstractBaseUser:
    return UserFactory()


def test_todo_list_view_unauthenticated(client) -> None:
    response: HttpResponse = client.get(reverse('todos:todo-list'))

    assert response.status_code == 302
    assert response.url == f"{reverse('account_login')}?next=/todos/"


def test_todo_list_view_authenticated(client, testuser) -> None:
    client.force_login(testuser)
    response: TemplateResponse = client.get(reverse('todos:todo-list'))

    assert response.status_code == 200
    assertTemplateUsed(response, 'todos/todo_list.html')
    assert 'todos' in response.context


def test_todo_add_view_unauthenticated(client) -> None:
    response: HttpResponse = client.get(reverse('todos:todo-add'))

    assert response.status_code == 302
    assert response.url == f"{reverse('account_login')}?next=/todos/add/"


def test_todo_add_view_authenticated_get(client, testuser) -> None:
    client.force_login(testuser)
    response: TemplateResponse = client.get(reverse('todos:todo-add'))

    assert response.status_code == 200
    assertTemplateUsed(response, 'todos/todo_form.html')
    assert isinstance(response.context['form'], TodoForm)


def test_todo_add_view_authenticated_post(client, testuser):
    client.force_login(testuser)
    response: TemplateResponse = client.post(
        reverse('todos:todo-add'),
        {'text': 'some task for todo', 'is_completed': False},
    )

    assert response.status_code == 302
    assert response.url == reverse_lazy('todos:todo-list')
    assert Todo.objects.count() == 1
