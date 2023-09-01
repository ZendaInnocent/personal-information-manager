import pytest
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractBaseUser
from django.urls import reverse_lazy
from django.utils.text import slugify

from ..models import Note


@pytest.fixture()
def testuser() -> AbstractBaseUser:
    return get_user_model().objects.create(username='testuser')


@pytest.fixture()
def create_note(testuser) -> Note:
    return Note.objects.create(
        user=testuser,
        title='note for test',
        content='some content goes here',
    )


def test_note_user(testuser, create_note) -> None:
    """A note must have a user associated with it when saved."""
    note: Note = create_note

    assert note.user == testuser


def test_note_save_method(testuser) -> None:
    """Ensure a note has a slug when save()is called.

    Slug should be based on title of the note
    """

    note: Note = Note(
        user=testuser,
        title='note for test',
        content='some content goes here',
    )

    note.save()

    assert note.slug == slugify(note.title)


def test_note_string_method(create_note: Note) -> None:
    """Note string method should return a title of a note."""

    note: Note = create_note

    assert str(note) == note.title


def test_note_absolute_url(create_note) -> None:
    """Ensure a note absolute url is the same as note detail url."""

    note: Note = create_note

    assert note.get_absolute_url() == reverse_lazy(
        'notes:note-detail', kwargs={'slug': note.slug}
    )
