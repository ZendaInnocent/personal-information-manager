import pytest
from django.contrib.auth.base_user import AbstractBaseUser

from ...accounts.tests.factories import UserFactory
from ..forms import TodoForm


@pytest.fixture()
def testuser() -> AbstractBaseUser:
    return UserFactory()


def test_invalid_todo_form() -> None:
    form = TodoForm(
        {
            'text': 'soem other thext',
        }
    )

    assert not form.is_valid()


def test_valid_todo_form(testuser):
    form = TodoForm(
        {
            'text': 'some tod text',
            'user': testuser,
            'is_completed': False,
        }
    )

    assert form.is_valid()
