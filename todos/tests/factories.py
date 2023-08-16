import factory

from accounts.tests.factories import UserFactory
from todos.models import Todo


class TodoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Todo

    user = UserFactory()
