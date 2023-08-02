from typing import Any

from django.db import models
from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView

from . import forms
from .models import Note


def index(request):
    notes = Note.objects.all()
    context = {'notes': notes}
    return render(request, 'notes/index.html', context)


class NoteCreateView(CreateView):
    model = Note
    form_class = forms.NoteForm


class NoteDetailView(DetailView):
    model = Note
