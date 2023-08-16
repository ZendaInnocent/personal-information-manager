from accounts.tests.factories import UserFactory


class TestTodosModel:
    def test_factory(self):
        user = UserFactory()

        assert user is not None
