from pim.accounts.tests.factories import UserFactory
from pim.todos.tests.factories import TodoFactory


class TestTodosModel:
    def test_factory(self):
        user = UserFactory()
        todo = TodoFactory(user=user)

        assert todo is not None
