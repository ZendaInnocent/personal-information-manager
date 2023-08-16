from django.urls import resolve, reverse

from pim.todos import views


class TestTodosUrls:
    def test_todos_homepage_url_resolves(self):
        url = reverse('todos:todos-index')

        assert resolve(url).func == views.index

    def test_delete_todo_url_resolves(self):
        url = reverse('todos:delete-todo', kwargs={'id': 1})

        assert resolve(url).func == views.delete_todo

    def test_toggle_todo_url_resolves(self):
        url = reverse('todos:toggle-todo', kwargs={'id': 1})

        assert resolve(url).func == views.toggle_todo

    def test_update_todo_url_resolves(self):
        url = reverse('todos:update-todo', kwargs={'id': 1})

        assert resolve(url).func == views.update_todo

    def test_sort_todos_url_resolves(self):
        url = reverse('todos:sort-todos')

        assert resolve(url).func == views.sort_todos
