from accounts.tests.factories import UserFactory
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed
from todos.tests.factories import TodoFactory


class TestTodosViews:
    def test_index_view_unauthenticated(self, client):
        response = client.get(reverse('todos:todos-index'))

        assert response.status_code == 302
        assert response.url == '/accounts/login/?next=/todos/'

    def test_index_view_authenticated(self, client):
        user = UserFactory()
        client.force_login(user)
        url = reverse('todos:todos-index')
        response = client.get(url)

        assert response.status_code == 200
        assertTemplateUsed(response, 'todos/index.html')

    def test_create_todo_unauthenticated(self, client):
        url = reverse('todos:todos-index')
        response = client.get(url)

        assert response.status_code == 302
        assert response.url == '/accounts/login/?next=/todos/'

    def test_create_todo(self, client):
        user = UserFactory()
        client.force_login(user)
        url = reverse('todos:todos-index')
        response = client.post(
            url,
            data={
                'todo': 'some todo text',
                'user': user,
            },
        )

        assert response.status_code == 200
        assertTemplateUsed(response, 'todos/partials/list.html')
        assert response.context['user_todos']

    def test_delete_todo(self, client):
        user = UserFactory()
        client.force_login(user)
        todo = TodoFactory(user=user)
        url = reverse(
            'todos:todo-delete',
            kwargs={'id': todo.id},
        )

        response = client.delete(url)

        assert response.status_code == 200
