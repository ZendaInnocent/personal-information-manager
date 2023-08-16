import factory

from pim.accounts.tests.factories import UserFactory
from pim.todos.models import Todo


class TodoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Todo

    user = UserFactory()
