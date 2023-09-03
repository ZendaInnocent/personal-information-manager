import pytest
from django.contrib.auth import get_user_model
from django.contrib.auth.base_user import AbstractBaseUser
from django.http import HttpResponse
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed

from ..models import Note


@pytest.fixture()
def testuser() -> AbstractBaseUser:
    return get_user_model().objects.create(username='testuser')


def test_notes_index_unauthenticated(client) -> None:
    """User must be logged in to access the page.

    Unauthenticated user should be redirected to the login page.
    """

    response: HttpResponse = client.get(reverse('notes:notes-index'))

    assert response.status_code == 302
    assert response.url == '/accounts/login/?next=/notes/'


def test_notes_index_authenticated(client, testuser) -> None:
    client.force_login(testuser)
    response: HttpResponse = client.get(reverse('notes:notes-index'))

    assert response.status_code == 200
    assertTemplateUsed(response, 'notes/index.html')


def test_note_create_view_initial_data(client, testuser) -> None:
    '''Ensure user is set as initial data.'''
    client.force_login(testuser)
    response: HttpResponse = client.get(reverse('notes:note-create'))

    assert response.status_code == 200
    assert response.context['form'].initial['user'] == testuser


def test_note_detail_view_test_func(client, testuser) -> None:
    '''Raises Permission denied when user try to access the note of other user.'''
    user: AbstractBaseUser = get_user_model().objects.create(username='username')
    note = Note.objects.create(user=user, title='some title', content='some content')

    client.force_login(testuser)
    response: HttpResponse = client.get(
        reverse('notes:note-detail', kwargs={'slug': note.slug})
    )

    assert response.status_code == 403


def test_note_update_view_test_func(client, testuser) -> None:
    '''Raises Permission denied when user try to update the note of other user.'''
    user: AbstractBaseUser = get_user_model().objects.create(username='username')
    note = Note.objects.create(user=user, title='some title', content='some content')

    client.force_login(testuser)
    response: HttpResponse = client.post(
        reverse('notes:note-update', kwargs={'slug': note.slug})
    )

    assert response.status_code == 403


def test_note_delete_view_test_func(client, testuser) -> None:
    '''Raises Permission denied when user try to delete the note of other user.'''
    user: AbstractBaseUser = get_user_model().objects.create(username='username')
    note = Note.objects.create(user=user, title='some title', content='some content')

    client.force_login(testuser)
    response: HttpResponse = client.delete(
        reverse('notes:note-delete', kwargs={'slug': note.slug})
    )

    assert response.status_code == 403
