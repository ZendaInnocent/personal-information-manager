import pytest
from django.contrib.auth.models import AbstractBaseUser
from django.http import HttpResponse
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed

from pim.accounts.tests.factories import UserFactory


@pytest.fixture()
def testuser() -> AbstractBaseUser:
    return UserFactory()


def test_index_view_unauthenticated(client) -> None:
    response: HttpResponse = client.get(reverse('todos:todos-index'))

    assert response.status_code == 302
    assert response.url == '/accounts/login/?next=/todos/'


def test_index_view_authenticated(client) -> None:
    user = UserFactory()
    client.force_login(user)
    url = reverse('todos:todos-index')
    response: HttpResponse = client.get(url)

    assert response.status_code == 200
    assertTemplateUsed(response=response, template_name='todos/index.html')


def test_create_todo_unauthenticated(client) -> None:
    url = reverse('todos:create-todo')
    response: HttpResponse = client.get(url)

    assert response.status_code == 302
    assert response.url == '/accounts/login/?next=/todos/create/'
