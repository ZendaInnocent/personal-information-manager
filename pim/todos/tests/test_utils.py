import pytest
from django.contrib.auth import get_user_model
from django.contrib.auth.base_user import AbstractBaseUser

from ..models import Todo
from ..utils import get_order_value


@pytest.fixture()
def testuser() -> AbstractBaseUser:
    return get_user_model().objects.create(username='testuser')


def test_get_order_value_method_for_first_item(testuser) -> None:
    order = get_order_value(testuser)

    assert 1 == order


def test_get_order_value_method_for_non_first_item(testuser) -> None:
    Todo.objects.create(user=testuser, text='some text')
    Todo.objects.create(user=testuser, text='some text')
    Todo.objects.create(user=testuser, text='some text')
    order = get_order_value(testuser)

    assert 4 == order
